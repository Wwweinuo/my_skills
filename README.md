# My Skills

这是我的 Claude Code 个人技能集合，基于 [Anthropic Skills](https://github.com/anthropics/skills) 插件体系扩展。

涵盖 **20 个技能**，包括文档处理、创意设计、API 开发、内容协作、学习教学和技能开发等领域。本项目特别强化了中文用户的使用体验，并加入了自定义学习类技能（如费曼学习法、多会话教学等）。

每个 Skill 是自包含的文件夹，包含 `SKILL.md` 指令文件以及配套的脚本和资源。

## 技能列表

| 类别 | 技能 | 说明 |
|------|------|------|
| 文档处理 | docx, pptx, xlsx, pdf | 创建、编辑、操作 Office 文档和 PDF |
| 创意与设计 | algorithmic-art, canvas-design, frontend-design, theme-factory, slack-gif-creator, brand-guidelines | 视觉设计、生成艺术、主题风格 |
| 开发与 API | claude-api, mcp-builder, web-artifacts-builder, webapp-testing, karpathy-guidelines | Claude API 开发、MCP 服务构建、Web 测试、编码规范 |
| 内容与协作 | doc-coauthoring, internal-comms, teach | 文档协作、内部通讯、技能教学 |
| 学习与效率 | feynman-technique | 费曼学习法、概念理解 |
| 技能开发 | skill-creator | 创建、优化和评测 Skill |

## 项目结构

```
├── .claude-plugin/marketplace.json   # 插件市场注册配置
├── skills/                            # 所有技能目录
│   ├── GUIDE.md                       # 技能分类指南
│   ├── <skill-name>/                  # 每个技能自包含文件夹
│   │   ├── SKILL.md                   # 技能定义（含 YAML frontmatter）
│   │   └── scripts/                   # 辅助脚本
│   └── ...
├── template/SKILL.md                  # 新技能模板
└── spec/                              # Agent Skills 规范
```

## 使用方式

在 Claude Code 中注册此仓库作为插件市场：

```
/plugin marketplace add Wwweinuo/my_skills
```

或直接安装插件：

```
/plugin install productivity-skills@anthropic-agent-skills
```

## 自定义技能亮点

- **[feynman-technique](./skills/feynman-technique)** — 费曼学习法，用最简单的语言解释复杂概念
- **[teach](./skills/teach)** — 多会话教学，在工作区内系统化学习新技能
- **[karpathy-guidelines](./skills/karpathy-guidelines)** — Karpathy 编码原则，减少常见 LLM 编码错误

## 许可

- docx, pptx, xlsx, pdf — **Source-available**（源可用）
- karpathy-guidelines — **MIT**
- feynman-technique — **Apache 2.0**
- 其余所有技能 — **Apache 2.0**
