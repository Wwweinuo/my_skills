# My Skills

这是 Wwweinuo 用来集中管理、验证和分发个人 Agent Skills 的 Git 仓库。每个 Skill 都是一个自包含目录，以 `SKILL.md` 作为入口，可附带脚本、参考资料和资源。

仓库同时保留部分第三方示例 Skill 作为参考。它们各自的许可证优先于仓库根许可证；发布或再分发前请阅读 [THIRD_PARTY_NOTICES.md](./THIRD_PARTY_NOTICES.md)。

## 使用

在 Claude Code 中添加 GitHub Marketplace：

```text
/plugin marketplace add Wwweinuo/my_skills
/plugin install personal-skills@wwweinuo-skills
```

本地开发时也可以直接添加仓库目录：

```text
/plugin marketplace add D:/code/my_skills
/plugin install personal-skills@wwweinuo-skills
```

更新远端内容后，刷新 Marketplace：

```text
/plugin marketplace update wwweinuo-skills
```

## 仓库结构

```text
├── .claude-plugin/marketplace.json  # Claude Code Marketplace
├── .github/workflows/validate.yml   # GitHub 自动校验
├── scripts/                         # 仓库维护工具
├── skills/
│   ├── catalog.json                 # 技能清单的唯一结构化数据源
│   ├── GUIDE.md                     # 面向读者的分类指南
│   └── <skill-name>/SKILL.md        # Skill 入口
├── template/SKILL.md                # 新 Skill 模板
├── LICENSE                          # 仓库原创内容许可证
└── THIRD_PARTY_NOTICES.md           # 第三方来源和发布限制
```

完整技能列表及分类见 [Skills 指南](./skills/GUIDE.md)，机器可读信息见 [`skills/catalog.json`](./skills/catalog.json)。

## 新增 Skill

```powershell
python scripts/new_skill.py my-skill `
  --description "说明它做什么，以及什么时候应当使用" `
  --category "开发与 API" `
  --summary "一句话简介" `
  --origin personal
```

然后完善生成的 `skills/my-skill/SKILL.md`，在 `skills/GUIDE.md` 对应分类中加入说明，并执行：

```powershell
python -m pip install -r requirements-dev.txt
python scripts/validate_repo.py
claude plugin validate .
```

## 许可证

仓库原创内容默认采用 [Apache License 2.0](./LICENSE)。Skill 目录内存在 `LICENSE.txt` 时，以该文件为准。特别注意：`docx`、`pptx`、`xlsx`、`pdf` 的现有条款不是开源许可证，并包含严格的复制和分发限制；`doc-coauthoring` 当前没有许可证文件，必须先核实授权再公开分发。
