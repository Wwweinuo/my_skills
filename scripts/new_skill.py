#!/usr/bin/env python3
"""Create a Skill directory and register it in the repository manifests."""

from __future__ import annotations

import argparse
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
SKILLS_DIR = ROOT / "skills"
CATALOG_PATH = SKILLS_DIR / "catalog.json"
MARKETPLACE_PATH = ROOT / ".claude-plugin" / "marketplace.json"
NAME_PATTERN = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")


def write_json(path: Path, value: dict) -> None:
    path.write_text(json.dumps(value, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("name")
    parser.add_argument("--description", required=True)
    parser.add_argument("--category", required=True)
    parser.add_argument("--summary", required=True)
    parser.add_argument("--origin", default="personal")
    parser.add_argument("--license", default="Apache-2.0-root", dest="license_name")
    parser.add_argument(
        "--not-redistributable",
        action="store_true",
        help="Mark the Skill as unsuitable for redistribution.",
    )
    args = parser.parse_args()

    if len(args.name) > 64 or not NAME_PATTERN.fullmatch(args.name):
        parser.error("name must be at most 64 characters of kebab-case")
    if len(args.description) > 1024 or "<" in args.description or ">" in args.description:
        parser.error("description must be at most 1024 characters without angle brackets")

    skill_dir = SKILLS_DIR / args.name
    if skill_dir.exists():
        parser.error(f"Skill already exists: {skill_dir.relative_to(ROOT)}")

    catalog = json.loads(CATALOG_PATH.read_text(encoding="utf-8"))
    if any(item.get("name") == args.name for item in catalog["skills"]):
        parser.error(f"Catalog already contains {args.name}")

    marketplace = json.loads(MARKETPLACE_PATH.read_text(encoding="utf-8"))
    plugins = marketplace.get("plugins", [])
    if len(plugins) != 1 or plugins[0].get("name") != "personal-skills":
        parser.error("Expected exactly one personal-skills plugin")

    skill_dir.mkdir()
    skill_content = (
        "---\n"
        f"name: {args.name}\n"
        f"description: {json.dumps(args.description, ensure_ascii=False)}\n"
        "---\n\n"
        f"# {args.name}\n\n"
        "Describe the outcome, essential workflow, and non-obvious constraints.\n\n"
        "## Verification\n\n"
        "Describe observable checks that demonstrate a correct result.\n"
    )
    (skill_dir / "SKILL.md").write_text(skill_content, encoding="utf-8")

    catalog["skills"].append(
        {
            "name": args.name,
            "category": args.category,
            "summary": args.summary,
            "origin": args.origin,
            "license": args.license_name,
            "redistributable": not args.not_redistributable,
        }
    )
    catalog["skills"].sort(key=lambda item: item["name"])
    write_json(CATALOG_PATH, catalog)

    skill_path = f"./skills/{args.name}"
    plugins[0]["skills"].append(skill_path)
    plugins[0]["skills"].sort()
    write_json(MARKETPLACE_PATH, marketplace)

    print(f"Created {skill_dir.relative_to(ROOT)}")
    print("Next: complete SKILL.md, add the GUIDE.md section, then run scripts/validate_repo.py")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
