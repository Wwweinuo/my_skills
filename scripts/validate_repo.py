#!/usr/bin/env python3
"""Validate the repository's Skill metadata and distribution manifests."""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("ERROR: PyYAML is required. Run: python -m pip install -r requirements-dev.txt")
    raise SystemExit(2)


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
ALLOWED_FRONTMATTER = {
    "name",
    "description",
    "license",
    "allowed-tools",
    "metadata",
    "compatibility",
    "when_to_use",
    "argument-hint",
    "arguments",
    "disable-model-invocation",
    "user-invocable",
    "model",
    "effort",
    "context",
    "agent",
    "background",
    "hooks",
    "paths",
    "shell",
}
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
FRONTMATTER_PATTERN = re.compile(r"\A---\s*\r?\n(.*?)\r?\n---(?:\s*\r?\n|\Z)", re.DOTALL)


def load_json(path: Path, errors: list[str]) -> dict:
    try:
        return json.loads(path.read_text(encoding="utf-8"))
    except FileNotFoundError:
        errors.append(f"缺少文件: {path.relative_to(ROOT)}")
    except json.JSONDecodeError as exc:
        errors.append(f"JSON 无效: {path.relative_to(ROOT)}:{exc.lineno}:{exc.colno}: {exc.msg}")
    return {}


def validate_skill(skill_dir: Path, errors: list[str], warnings: list[str]) -> None:
    relative = skill_dir.relative_to(ROOT)
    skill_file = skill_dir / "SKILL.md"
    if not skill_file.is_file():
        errors.append(f"{relative} 缺少 SKILL.md")
        return

    content = skill_file.read_text(encoding="utf-8")
    match = FRONTMATTER_PATTERN.match(content)
    if not match:
        errors.append(f"{relative}/SKILL.md 缺少有效的 YAML frontmatter")
        return

    try:
        metadata = yaml.safe_load(match.group(1))
    except yaml.YAMLError as exc:
        errors.append(f"{relative}/SKILL.md frontmatter 无法解析: {exc}")
        return

    if not isinstance(metadata, dict):
        errors.append(f"{relative}/SKILL.md frontmatter 必须是对象")
        return

    unexpected = sorted(set(metadata) - ALLOWED_FRONTMATTER)
    if unexpected:
        errors.append(f"{relative}/SKILL.md 包含不支持的字段: {', '.join(unexpected)}")

    name = metadata.get("name")
    description = metadata.get("description")
    if not isinstance(name, str) or not name.strip():
        errors.append(f"{relative}/SKILL.md 缺少非空 name")
    else:
        name = name.strip()
        if name != skill_dir.name:
            errors.append(f"{relative}/SKILL.md 的 name={name!r} 与目录名不一致")
        if len(name) > 64 or not NAME_PATTERN.fullmatch(name):
            errors.append(f"{relative}/SKILL.md 的 name 必须是最长 64 字符的 kebab-case")

    if not isinstance(description, str) or not description.strip():
        errors.append(f"{relative}/SKILL.md 缺少非空 description")
    else:
        description = description.strip()
        if len(description) > 1536:
            errors.append(f"{relative}/SKILL.md 的 description 超过 Claude Code 的 1536 字符上限")
        elif len(description) > 1024:
            warnings.append(f"{relative}/SKILL.md 的 description 超过通用 Agent Skills 规范建议的 1024 字符")
        if "<" in description or ">" in description:
            errors.append(f"{relative}/SKILL.md 的 description 不得包含尖括号")

    line_count = len(content.splitlines())
    if line_count > 500:
        warnings.append(f"{relative}/SKILL.md 共 {line_count} 行；建议把条件化细节移入 references/")


def validate_catalog(
    catalog: dict,
    folder_names: set[str],
    errors: list[str],
    warnings: list[str],
    strict_distribution: bool,
) -> set[str]:
    if catalog.get("schemaVersion") != 1:
        errors.append("skills/catalog.json 的 schemaVersion 必须为 1")

    entries = catalog.get("skills")
    if not isinstance(entries, list):
        errors.append("skills/catalog.json 的 skills 必须是数组")
        return set()

    required = {"name", "category", "summary", "origin", "license", "redistributable"}
    names: list[str] = []
    for index, entry in enumerate(entries):
        if not isinstance(entry, dict):
            errors.append(f"skills/catalog.json skills[{index}] 必须是对象")
            continue
        missing = sorted(required - set(entry))
        if missing:
            errors.append(f"skills/catalog.json skills[{index}] 缺少字段: {', '.join(missing)}")
        name = entry.get("name")
        if isinstance(name, str):
            names.append(name)
        if entry.get("redistributable") is False and isinstance(name, str):
            message = f"{name} 标记为不可再分发；公开发布前应移除或确认授权"
            (errors if strict_distribution else warnings).append(message)
        if "redistributable" in entry and not isinstance(entry["redistributable"], bool):
            errors.append(f"skills/catalog.json skills[{index}].redistributable 必须是布尔值")
        license_name = entry.get("license")
        if isinstance(name, str) and isinstance(license_name, str):
            license_file = SKILLS_DIR / name / "LICENSE.txt"
            if not license_name.endswith("-root") and license_name != "Unverified" and not license_file.is_file():
                errors.append(f"{name} 声明许可证 {license_name}，但目录内缺少 LICENSE.txt")

    name_set = set(names)
    duplicates = sorted({name for name in names if names.count(name) > 1})
    if duplicates:
        errors.append(f"skills/catalog.json 存在重复名称: {', '.join(duplicates)}")
    if names != sorted(names):
        errors.append("skills/catalog.json 的 skills 必须按 name 排序")
    if name_set != folder_names:
        missing = sorted(folder_names - name_set)
        extra = sorted(name_set - folder_names)
        if missing:
            errors.append(f"Catalog 缺少技能: {', '.join(missing)}")
        if extra:
            errors.append(f"Catalog 引用了不存在的技能: {', '.join(extra)}")
    return name_set


def validate_marketplace(manifest: dict, folder_names: set[str], errors: list[str]) -> None:
    if manifest.get("name") != "wwweinuo-skills":
        errors.append("Marketplace 名称必须是 wwweinuo-skills")
    owner = manifest.get("owner")
    if not isinstance(owner, dict) or owner.get("name") != "Wwweinuo":
        errors.append("Marketplace owner.name 必须是 Wwweinuo")

    plugins = manifest.get("plugins")
    if not isinstance(plugins, list) or not plugins:
        errors.append("Marketplace 必须至少包含一个插件")
        return

    referenced: list[str] = []
    for plugin in plugins:
        if not isinstance(plugin, dict):
            errors.append("Marketplace plugin 条目必须是对象")
            continue
        for raw_path in plugin.get("skills", []):
            if not isinstance(raw_path, str) or not raw_path.startswith("./skills/"):
                errors.append(f"Marketplace Skill 路径无效: {raw_path!r}")
                continue
            referenced.append(raw_path.removeprefix("./skills/"))

    if len(referenced) != len(set(referenced)):
        errors.append("Marketplace 存在重复的 Skill 引用")
    referenced_set = set(referenced)
    if referenced_set != folder_names:
        missing = sorted(folder_names - referenced_set)
        extra = sorted(referenced_set - folder_names)
        if missing:
            errors.append(f"Marketplace 缺少技能: {', '.join(missing)}")
        if extra:
            errors.append(f"Marketplace 引用了不存在的技能: {', '.join(extra)}")


def validate_guide(folder_names: set[str], errors: list[str]) -> None:
    guide_path = SKILLS_DIR / "GUIDE.md"
    if not guide_path.is_file():
        errors.append("缺少 skills/GUIDE.md")
        return
    guide = guide_path.read_text(encoding="utf-8")
    headings = set(re.findall(r"^### \[([a-z0-9-]+)\]\(\./[^)]+\)", guide, re.MULTILINE))
    if headings != folder_names:
        missing = sorted(folder_names - headings)
        extra = sorted(headings - folder_names)
        if missing:
            errors.append(f"GUIDE 缺少技能章节: {', '.join(missing)}")
        if extra:
            errors.append(f"GUIDE 包含不存在的技能章节: {', '.join(extra)}")


def run_claude_validation(errors: list[str]) -> None:
    executable = shutil.which("claude")
    if not executable:
        errors.append("未找到 claude，无法运行官方插件校验")
        return
    result = subprocess.run(
        [executable, "plugin", "validate", "."],
        cwd=ROOT,
        text=True,
        encoding="utf-8",
        errors="replace",
        capture_output=True,
        check=False,
    )
    if result.returncode != 0:
        output = (result.stdout + result.stderr).strip()
        errors.append(f"claude plugin validate 失败:\n{output}")


def main() -> int:
    if hasattr(sys.stdout, "reconfigure"):
        sys.stdout.reconfigure(encoding="utf-8")
        sys.stderr.reconfigure(encoding="utf-8")
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--strict-distribution",
        action="store_true",
        help="Treat non-redistributable skills as errors.",
    )
    parser.add_argument(
        "--with-claude",
        action="store_true",
        help="Also run the installed Claude Code validator.",
    )
    args = parser.parse_args()

    errors: list[str] = []
    warnings: list[str] = []
    skill_dirs = sorted(path for path in SKILLS_DIR.iterdir() if path.is_dir())
    folder_names = {path.name for path in skill_dirs}

    for skill_dir in skill_dirs:
        validate_skill(skill_dir, errors, warnings)

    catalog = load_json(SKILLS_DIR / "catalog.json", errors)
    validate_catalog(catalog, folder_names, errors, warnings, args.strict_distribution)
    manifest = load_json(ROOT / ".claude-plugin" / "marketplace.json", errors)
    validate_marketplace(manifest, folder_names, errors)
    validate_guide(folder_names, errors)

    if not (ROOT / "LICENSE").is_file():
        errors.append("仓库根目录缺少 LICENSE")
    if not (ROOT / "NOTICE").is_file():
        errors.append("仓库根目录缺少 NOTICE")
    if not (ROOT / "THIRD_PARTY_NOTICES.md").is_file():
        errors.append("仓库根目录缺少 THIRD_PARTY_NOTICES.md")
    if args.with_claude:
        run_claude_validation(errors)

    for warning in warnings:
        print(f"WARNING: {warning}")
    for error in errors:
        print(f"ERROR: {error}")

    if errors:
        print(f"\n校验失败: {len(errors)} 个错误，{len(warnings)} 个警告")
        return 1
    print(f"\n校验通过: {len(skill_dirs)} 个 Skill，{len(warnings)} 个警告")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
