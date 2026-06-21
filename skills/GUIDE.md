# Skills 指南

本仓库包含 17 个 Skill，涵盖文档处理、创意设计、API 开发、内容协作和技能开发等领域。每个 Skill 是自包含的文件夹，包含 `SKILL.md` 指令文件以及配套的脚本和资源。

---

## 分类总览

| 类别 | Skills | 用途 |
|------|--------|------|
| 文档处理 | docx, pptx, xlsx, pdf | 创建、编辑、操作 Office 文档和 PDF |
| 创意与设计 | algorithmic-art, canvas-design, frontend-design, theme-factory, slack-gif-creator, brand-guidelines | 视觉设计、生成艺术、主题风格 |
| 开发与 API | claude-api, mcp-builder, web-artifacts-builder, webapp-testing | Claude API 开发、MCP 服务构建、Web 测试 |
| 内容与协作 | doc-coauthoring, internal-comms | 文档协作文档、内部通讯撰写 |
| 技能开发工具 | skill-creator | 创建、优化和评测 Skill |

---

## 一、文档处理

### [docx](./docx)
- **描述**: 创建、读取、编辑和操作 Word 文档（.docx）
- **功能**: 文档生成、内容提取、图片插入替换、修订与评论、邮件合并
- **许可**: Source-available
- **关键文件**: `scripts/office/`（OOXML 打包解包、XSD 校验、修订处理）

### [pptx](./pptx)
- **描述**: 创建、编辑和操作 PowerPoint 演示文稿（.pptx）
- **功能**: 幻灯片创建、内容提取、模板应用、设计建议、缩略图生成
- **许可**: Source-available
- **关键文件**: `scripts/office/`（与 docx 共享 OOXML 工具库）、`scripts/thumbnail.py`

### [xlsx](./xlsx)
- **描述**: 创建、读取、编辑和修复电子表格（.xlsx/.xlsm/.csv/.tsv）
- **功能**: 表格读写、公式计算、数据清洗、格式转换
- **许可**: Source-available
- **关键文件**: `scripts/office/`（共享工具库）、`scripts/recalc.py`

### [pdf](./pdf)
- **描述**: 读取、创建和操作 PDF 文件
- **功能**: 文本/表格提取、合并拆分、表单填写、加密解密、OCR、水印
- **许可**: Source-available
- **关键文件**: `scripts/`（表单处理、边界检查、图片转换等 Python 脚本）

---

## 二、创意与设计

### [algorithmic-art](./algorithmic-art)
- **描述**: 使用 p5.js 创建算法生成艺术
- **功能**: 流场、粒子系统、种子随机数、交互式参数探索
- **许可**: Apache 2.0
- **关键文件**: `templates/generator_template.js`、`templates/viewer.html`

### [canvas-design](./canvas-design)
- **描述**: 用 Canvas 创建精美的 PNG/PDF 视觉设计作品
- **功能**: 海报设计、多页面布局、排版与配色
- **许可**: Apache 2.0
- **关键文件**: `canvas-fonts/`（40+ 中英文字体文件）

### [frontend-design](./frontend-design)
- **描述**: 构建独特且有意的 UI 视觉设计
- **功能**: 设计原则、排版指导、审美方向
- **许可**: Apache 2.0

### [theme-factory](./theme-factory)
- **描述**: 为幻灯片、文档、HTML 页面等应用主题风格
- **功能**: 10 套预设主题（极光冰霜、森林 canopy、午夜银河等），支持即时生成新主题
- **许可**: Apache 2.0
- **关键文件**: `themes/`（10 个主题定义文件）、`theme-showcase.pdf`

### [slack-gif-creator](./slack-gif-creator)
- **描述**: 创建适用于 Slack 的动画 GIF
- **功能**: GIF 构建、帧合成、缓动函数、Slack 尺寸验证
- **许可**: Apache 2.0
- **关键文件**: `core/`（easing.py, frame_composer.py, gif_builder.py, validators.py）

### [brand-guidelines](./brand-guidelines)
- **描述**: 应用 Anthropic 官方品牌色和字体
- **功能**: 品牌色彩系统、字体应用、形状与强调色
- **许可**: Apache 2.0

---

## 三、开发与 API

### [claude-api](./claude-api)
- **描述**: Claude API / Anthropic SDK 完整参考
- **覆盖语言**: Python, TypeScript, Java, Go, Ruby, PHP, C#
- **覆盖主题**: 模型定价、流式传输、Tool Use、MCP、Agent、Prompt Caching、Token 计数、模型迁移、Managed Agents
- **许可**: Apache 2.0
- **关键文件**: `python/`、`typescript/`、`shared/`（跨语言通用文档）、`curl/`

### [mcp-builder](./mcp-builder)
- **描述**: 构建 MCP（Model Context Protocol）服务器的指导
- **功能**: Python (FastMCP) 和 Node/TypeScript (MCP SDK) 实现，工具设计评估
- **许可**: Apache 2.0
- **关键文件**: `reference/`（MCP 最佳实践、评估指南）、`scripts/`（连接测试、评估脚本）

### [web-artifacts-builder](./web-artifacts-builder)
- **描述**: 使用 React + Tailwind CSS + shadcn/ui 构建复杂的 claude.ai HTML 制品
- **功能**: 多组件制品初始化、打包、shadcn/ui 组件集成
- **许可**: Apache 2.0
- **关键文件**: `scripts/init-artifact.sh`、`scripts/bundle-artifact.sh`、`scripts/shadcn-components.tar.gz`

### [webapp-testing](./webapp-testing)
- **描述**: 使用 Playwright 测试本地 Web 应用
- **功能**: 前端功能验证、UI 行为调试、截图捕获、浏览器日志查看
- **许可**: Apache 2.0
- **关键文件**: `scripts/with_server.py`、`examples/`（控制台日志、元素发现、静态 HTML 自动化示例）

---

## 四、内容与协作

### [doc-coauthoring](./doc-coauthoring)
- **描述**: 引导用户完成文档合著的结构化工作流
- **功能**: PRD、设计文档、决策文档、RFC 等文档的类型化协作
- **阶段**: 上下文收集 → 细化与结构化 → 读者测试 → 终审
- **许可**: Apache 2.0

### [internal-comms](./internal-comms)
- **描述**: 编写各类内部通讯
- **功能**: 状态报告、领导层更新、第三方更新、公司简报、FAQ、事故报告、项目更新
- **许可**: Apache 2.0
- **关键文件**: `examples/`（各类型通讯模板）

---

## 五、技能开发工具

### [skill-creator](./skill-creator)
- **描述**: 创建、优化和评测 Skill
- **功能**: 从头创建 Skill、运行评测、基准测试与方差分析、描述优化、盲对比评测
- **许可**: Apache 2.0
- **关键文件**: `agents/`（analyzer/comparator/grader 代理定义）、`scripts/`（评测、报告、打包脚本）、`eval-viewer/`

---

## 许可说明

| 技能 | 许可 |
|------|------|
| docx, pptx, xlsx, pdf | **Source-available**（源可用，非开源） |
| 其余所有技能 | **Apache 2.0** |

## 快速导航

- **想创建技能？** → [skill-creator](./skill-creator)
- **想用文档格式？** → 对应格式技能 + [theme-factory](./theme-factory) 美化
- **想开发 Claude 应用？** → [claude-api](./claude-api) + [mcp-builder](./mcp-builder)
- **想设计 UI？** → [frontend-design](./frontend-design) + [brand-guidelines](./brand-guidelines) + [theme-factory](./theme-factory)
- **想测试 Web 应用？** → [webapp-testing](./webapp-testing)
- **想写文档/通讯？** → [doc-coauthoring](./doc-coauthoring) + [internal-comms](./internal-comms)
- **想生成艺术/GIF？** → [algorithmic-art](./algorithmic-art) + [canvas-design](./canvas-design) + [slack-gif-creator](./slack-gif-creator)
