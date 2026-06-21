# My Skills

该项目是 Claude Code Skills 插件仓库，通过 `.claude-plugin/marketplace.json` 注册多个插件（plugins），每个插件下包含若干技能（skills）。

## 项目结构

```
├── .claude-plugin/marketplace.json   # 插件市场注册配置
├── skills/                            # 所有技能目录
│   ├── GUIDE.md                       # 技能分类指南（新增技能后需同步更新）
│   ├── <skill-name>/                  # 每个技能自包含文件夹
│   │   ├── SKILL.md                   # 技能定义（含 YAML frontmatter: name, description, trigger）
│   │   ├── scripts/                   # 辅助脚本
│   │   └── ...
│   └── ...
├── template/SKILL.md                  # 新技能模板
└── spec/                              # Agent Skills 规范
```

## 关键规则

### 新增技能时必须更新 GUIDE.md

每次添加新技能（即在 `skills/` 下新建文件夹并编写 `SKILL.md` 后），必须同步更新 `skills/GUIDE.md`：

1. 在对应分类下添加新技能条目（或创建新分类）
2. 参考已有条目的格式，包含：描述、核心功能、许可类型、关键文件
3. 如果新技能不属于现有五大分类，增加新的分类
4. 确保分类总览表也同步更新
5. 底部的"快速导航"部分根据新技能的功能决定是否补充入口

### 技能文件规范

- 每个技能以文件夹形式存放在 `skills/` 下
- 必须包含 `SKILL.md`，带 YAML frontmatter（`name`、`description`）
- `template/SKILL.md` 可作为新技能的起点
- 许可文件（如有）统一命名为 `LICENSE.txt`

### 插件注册

新技能如需在市场中可见，需在 `.claude-plugin/marketplace.json` 中注册，添加到对应 plugin 的 `skills` 数组下，或创建新的 plugin 对象。
