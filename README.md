# 📚 WorkBuddy Skills

> 一个持续收集的 **WorkBuddy / Agent Skills** 技能合集，覆盖工程标准、工作流自动化等场景。每个技能独立成子文件夹，互不干扰，按需取用。

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-informational.svg)](#-已收录技能)
[![Updated](https://img.shields.io/badge/updated-2026--09-brightgreen.svg)](#)

## ✨ 为什么用这个合集

- **单一来源** —— 所有技能集中维护，避免散落各处、版本混乱
- **按需取用** —— 只克隆 / 复制你需要的技能子文件夹，不污染 WorkBuddy 配置
- **修订案优先** —— 标准类技能直接以最新修订案为准，旧条文标记为失效
- **持续扩展** —— 新技能以子文件夹形式加入，见下方「新增技能」

## 📦 已收录技能

| 技能 | 说明 | 标准 / 主题 |
| --- | --- | --- |
| [mh5001-2021-flight-area-standard](./mh5001-2021-flight-area-standard/) | 民用机场飞行区技术标准 MH5001-2021 主文 + 第一~第四修订案知识库 | MH 5001-2021 |

## 📂 仓库结构

```
workbuddy-skills/
├── README.md                            # 本文件（合集说明）
├── LICENSE                              # MIT 许可证
└── mh5001-2021-flight-area-standard/    # 技能：MH5001 飞行区标准
    ├── SKILL.md                         # 技能入口（frontmatter + 索引）
    ├── chapters/                        # 12 章摘要 ch01~ch12
    ├── glossary.md                      # 术语表（含 PCR/ACR）
    ├── patterns.md                      # 评价流程（ACR-PCR 等）
    ├── cheatsheet.md                    # 决策规则速查
    ├── amendments.md                    # 四份修订案覆盖登记
    └── README.md                        # 技能说明
```

## 🚀 快速开始

克隆仓库，把需要的技能子文件夹复制到 WorkBuddy 技能目录：

```bash
git clone https://github.com/LazyRa/workbuddy-skills.git

# 复制单个技能（macOS / Linux）
cp -r workbuddy-skills/mh5001-2021-flight-area-standard "$HOME/.workbuddy/skills/"

# Windows（PowerShell）
# Copy-Item -Recurse workbuddy-skills/mh5001-2021-flight-area-standard "$env:USERPROFILE\.workbuddy\skills\"
```

技能目录位置：

- **Windows**：`C:\Users\<用户名>\.workbuddy\skills\`
- **macOS / Linux**：`~/.workbuddy/skills/`

> 复制完成后**重启 WorkBuddy 会话**，技能即出现在技能列表中。

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

本项目以 [MIT 许可证](LICENSE) 开源。各技能所整理的第三方标准 / 文档，其版权归原著作权人所有，本合集仅作结构化整理，引用时请以规范正本为准。
