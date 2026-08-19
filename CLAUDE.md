# My Skills 仓库维护说明

这是 Wwweinuo 的个人 Agent Skills 仓库。`skills/` 是技能内容的唯一源目录，`.claude-plugin/marketplace.json` 负责 Claude Code 分发。

## 维护约束

- 不要覆盖用户尚未提交的修改。
- 每个 `skills/<name>/` 目录必须包含 `SKILL.md`。
- `SKILL.md` frontmatter 至少包含 `name` 和 `description`；目录名必须与 `name` 相同。
- `description` 需同时说明 Skill 的能力及适用时机。
- 详细的条件化说明放入 `references/`，可重复执行的确定性操作放入 `scripts/`，生成物素材放入 `assets/`。
- `skills/catalog.json` 是技能名称、分类、来源和许可证的唯一结构化数据源。
- 新增、删除或重命名 Skill 时，同步更新 `skills/catalog.json`、`skills/GUIDE.md` 和 Marketplace 的 `skills` 数组。
- Skill 目录内的许可证优先于仓库根许可证。不得把 source-available 内容描述成开源内容。
- 提交前运行 `python scripts/validate_repo.py`；安装 Claude Code 的环境还应运行 `claude plugin validate .`。

## 新建 Skill

优先使用 `scripts/new_skill.py` 创建目录和 Catalog 条目，再根据实际工作流完善内容。不要创建没有用途的空目录或示例文件。

## 第三方内容

来源和再分发限制记录在 `THIRD_PARTY_NOTICES.md`。修改第三方 Skill 时保留其许可证和署名，不要用根许可证覆盖 Skill 自带许可证。
