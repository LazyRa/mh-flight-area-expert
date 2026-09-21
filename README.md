# 📚 WorkBuddy Skills

> 一个持续收集的 **WorkBuddy / Agent Skills** 技能合集，覆盖民航工程标准、规章知识库与工作流自动化。每个技能独立成子文件夹，互不干扰，按需取用。

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-3-informational.svg)](#-已收录技能)
[![Updated](https://img.shields.io/badge/updated-2026--09-brightgreen.svg)](#)

## ✨ 为什么用这个合集

- **单一来源** —— 所有技能集中维护，避免散落各处、版本混乱
- **按需取用** —— 只克隆 / 复制你需要的技能子文件夹，不污染 WorkBuddy 配置
- **修订案优先** —— 标准 / 规章类技能直接以最新修订案、现行版本为准，旧条文标记为失效
- **可扩展知识库** —— 一个技能内可容纳多份规定（见 `mh-flight-area-expert`），并有配套入库工具
- **持续扩展** —— 新技能以子文件夹形式加入，见下方「新增技能」

## 📦 已收录技能

| 技能 | 说明 | 主题 |
| --- | --- | --- |
| [mh-flight-area-expert](./mh-flight-area-expert/) | 民航飞行区专家：**多规定知识库**，收录飞行区运行规章（含《运输机场运行安全管理规定》CCAR-139B 全 14 章），可跨规定定位、给带条款号的回答 | 飞行区运行规章 |
| [mh5001-2021-flight-area-standard](./mh5001-2021-flight-area-standard/) | 《民用机场飞行区技术标准 MH 5001-2021》主文 + 第一~第四修订案知识库 | MH 5001-2021 |
| [regulation-ingest](./regulation-ingest/) | 规章入库助手：把新的规章 PDF 自动提取、清洗、结构化，并入知识库（支持新增 / 更新两种流程） | 工具 / 工作流 |

## 📂 仓库结构

```
workbuddy-skills/
├── README.md                     # 本文件（合集说明）
├── LICENSE                       # MIT 许可证
├── mh-flight-area-expert/        # 技能：飞行区专家（多规定知识库）
│   ├── SKILL.md                  # 专家人设 + 模块地图 + 路由索引
│   ├── index/                    # by-doc / by-topic 总索引
│   ├── kb/                       # 知识库（按类别 / 规定分子模块）
│   ├── glossary.md               # 跨规定术语表
│   └── scripts/search.py         # 全文 / 条款号检索
├── mh5001-2021-flight-area-standard/   # 技能：MH5001 飞行区标准
│   ├── SKILL.md
│   ├── chapters/                 # 12 章摘要
│   ├── glossary.md / patterns.md / cheatsheet.md / amendments.md
│   └── README.md
└── regulation-ingest/            # 技能：规章入库助手
    ├── SKILL.md
    ├── ingest.config.json        # 目标知识库路径配置
    ├── assets/module-template.md
    └── scripts/ingest.py         # 提取 / 建模块 / 登记索引
```

## 🚀 快速开始

克隆仓库，把需要的技能子文件夹复制到 WorkBuddy 技能目录：

```bash
git clone https://github.com/LazyRa/workbuddy-skills.git

# 复制单个技能（macOS / Linux）
cp -r workbuddy-skills/mh-flight-area-expert "$HOME/.workbuddy/skills/"

# Windows（PowerShell）
# Copy-Item -Recurse workbuddy-skills\mh-flight-area-expert "$env:USERPROFILE\.workbuddy\skills\"
```

技能目录位置：

- **Windows**：`C:\Users\<用户名>\.workbuddy\skills\`
- **macOS / Linux**：`~/.workbuddy/skills/`

> 复制完成后**重启 WorkBuddy 会话**，技能即出现在技能列表中。

## 📥 往知识库加新规定

`mh-flight-area-expert` 支持持续扩充：把规章 PDF 交给 WorkBuddy，配合 `regulation-ingest` 技能即可自动提取、清洗、结构化并挂入索引。若是某规定的**新版本**，走「更新流程」并**全局搜索失效引用**。详见该技能的 `SKILL.md`。

## ➕ 新增一个技能

1. 在仓库根目录新建子文件夹（用技能 slug 命名，如 `my-new-skill/`）
2. 放入 `SKILL.md` 及配套文件
3. 在本 README 的「已收录技能」表格补一行
4. 提交并推送：

```bash
git add -A && git commit -m "Add skill: <slug>" && git push
```

## 🤝 贡献

欢迎通过 Issue / Pull Request 补充技能或修正内容。新增技能请遵循上方「新增技能」约定，并确保 `SKILL.md` 含合法的 frontmatter。

## 📄 许可证

本项目以 [MIT 许可证](LICENSE) 开源。各技能所整理的第三方标准 / 规章 / 文档，其版权归原著作权人所有，本合集仅作结构化整理，引用时请以规范正本为准。
