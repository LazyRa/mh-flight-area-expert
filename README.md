# 📚 WorkBuddy Skills

> 一个持续收集的 **WorkBuddy / Agent Skills** 技能合集，聚焦民航飞行区规章与技术标准知识库。每个技能独立成子文件夹，按需取用。

[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
[![Skills](https://img.shields.io/badge/skills-1-informational.svg)](#-已收录技能)
[![Updated](https://img.shields.io/badge/updated-2026--09-brightgreen.svg)](#)

## ✨ 为什么用这个合集

- **单一来源** —— 所有技能集中维护，避免散落各处、版本混乱
- **按需取用** —— 只克隆 / 复制你需要的技能子文件夹，不污染 WorkBuddy 配置
- **修订案优先** —— 标准 / 规章类技能直接以最新修订案、现行版本为准，旧条文标记为失效
- **可扩展知识库** —— 一个技能内可容纳多份规定（见 `mh-flight-area-expert`）
- **持续扩展** —— 新技能 / 新规定以子文件夹形式加入

## 📦 已收录技能

| 技能 | 说明 | 主题 |
| --- | --- | --- |
| [mh-flight-area-expert](./mh-flight-area-expert/) | 民航飞行区专家：**多规定知识库**，可跨规定定位、给带条款号的回答。已含《民用机场飞行区技术标准 MH 5001-2021》（含第一~第四修订案）与《运输机场运行安全管理规定》CCAR-139B（全 14 章） | 飞行区技术标准 + 运行规章 |

## 📂 仓库结构

```
workbuddy-skills/
├── README.md                     # 本文件（合集说明）
├── LICENSE                       # MIT 许可证
└── mh-flight-area-expert/        # 技能：飞行区专家（多规定知识库）
    ├── SKILL.md                  # 专家人设 + 模块地图 + 路由索引
    ├── index/                    # by-doc / by-topic 总索引
    ├── kb/                       # 知识库（按类别 / 规定分子模块）
    │   ├── 02-民航规章CCAR/运输机场运行安全管理规定/   # 14 章
    │   └── 03-行业标准MH/mh5001-2021/                 # 12 章（含四修订案）
    ├── glossary.md               # 跨规定术语表
    └── scripts/search.py         # 全文 / 条款号检索
```

## 🚀 快速开始

克隆仓库，把技能文件夹复制到 WorkBuddy 技能目录：

```bash
git clone https://github.com/LazyRa/workbuddy-skills.git

# macOS / Linux
cp -r workbuddy-skills/mh-flight-area-expert "$HOME/.workbuddy/skills/"

# Windows（PowerShell）
# Copy-Item -Recurse workbuddy-skills\mh-flight-area-expert "$env:USERPROFILE\.workbuddy\skills\"
```

技能目录位置：

- **Windows**：`C:\Users\<用户名>\.workbuddy\skills\`
- **macOS / Linux**：`~/.workbuddy/skills/`

> 复制完成后**重启 WorkBuddy 会话**，技能即出现在技能列表中。

## 📥 知识库如何扩充

`mh-flight-area-expert` 采用"**一个技能、多份规定**"结构：

1. 在 `kb/<类别>/<规定>/` 下新建模块（`MODULE.md` + `chapters/` + `source.txt`）
2. 在 `index/by-doc.md`（文档清单）与 `index/by-topic.md`（主题索引）补登记
3. 在 `SKILL.md` 的「模块地图」与「路由索引」补一行
4. 若是**版本更新**：另需**全局搜索并更新失效引用**（旧条款 / 旧术语）

类别目录：`01-法律法规` / `02-民航规章CCAR` / `03-行业标准MH` / `04-咨询通告AC` / `05-ICAO`

## ➕ 新增一个技能

1. 在仓库根目录新建子文件夹（用技能 slug 命名）
2. 放入 `SKILL.md` 及配套文件
3. 在本 README 的「已收录技能」表格补一行
4. `git add -A && git commit -m "Add skill: <slug>" && git push`

## 🤝 贡献

欢迎通过 Issue / Pull Request 补充技能或修正内容。新增技能请遵循上方约定，并确保 `SKILL.md` 含合法的 frontmatter。

## 📄 许可证

本项目以 [MIT 许可证](LICENSE) 开源。各技能所整理的第三方标准 / 规章 / 文档，其版权归原著作权人所有，本合集仅作结构化整理，引用时请以规范正本为准。
