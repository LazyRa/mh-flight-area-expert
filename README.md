# 民航飞行区专家

> 一个 WorkBuddy / Agent Skills 知识库技能：把**民航飞行区运行规章与技术标准**整理成可检索、可问答、有边界的结构化知识。**一个技能、多份规定**，可跨规定定位并给出带条款号的回答。

[![Standard](https://img.shields.io/badge/standards-MH%205001--2021%20%7C%20CCAR--139B-blue.svg)](#-已收录规定)
[![Amendments](https://img.shields.io/badge/amendments-1~4-green.svg)](#修订案覆盖)
[![License: MIT](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)

## ✨ 特性

- **多规定知识库**：一个技能内按 `kb/<类别>/<规定>/` 组织，跨规定主题用 `index/by-topic.md` 定位
- **修订案优先**：MH5001-2021 直接以第一~第四修订案为准，旧条文（PCN/ACN 等）标记为失效
- **现行版本可判**：`index/by-doc.md` 给出每份规定的现行/失效状态与施行日期
- **回答有规范**：先定位 → 引条款号 → 判现行版本 → 给结论 → 超范围直说"未收录"
- **可检索**：`scripts/search.py` 支持全文 / 条款号检索

## 📦 已收录规定

| 类别 | 规定 | 版本状态 |
| --- | --- | --- |
| 03-行业标准MH | 民用机场飞行区技术标准（MH 5001-2021） | 现行（含第一~第四修订案，以修订案为准） |
| 02-民航规章CCAR | 运输机场运行安全管理规定（CCAR-139B） | 现行（交通运输部令 2025 年第 5 号，2026-07-01 施行） |

## 📂 目录结构

```
mh-flight-area-expert/
├── SKILL.md                       # 技能入口：专家人设 + 模块地图 + 路由索引
├── index/
│   ├── by-doc.md                  # 文档清单（含现行/失效状态）
│   └── by-topic.md                # 主题索引（跨规定定位）
├── kb/                            # 知识库（按类别 / 规定分子模块）
│   ├── 02-民航规章CCAR/运输机场运行安全管理规定/   # 14 章
│   └── 03-行业标准MH/mh5001-2021/                 # 12 章（含四修订案）
├── glossary.md                    # 跨规定术语表
└── scripts/search.py              # 全文 / 条款号检索
```

每个模块含：`MODULE.md`（元数据 / 覆盖范围 / 章节目录 / 交叉引用 / 版本历史）、`source.txt`（提取正文）、`chapters/`。

## 🚀 安装

直接把仓库克隆到 WorkBuddy 技能目录（仓库根即技能根）：

```bash
# macOS / Linux
git clone https://github.com/LazyRa/mh-flight-area-expert.git \
  "$HOME/.workbuddy/skills/mh-flight-area-expert"

# Windows（PowerShell）
# git clone https://github.com/LazyRa/mh-flight-area-expert.git "$env:USERPROFILE\.workbuddy\skills\mh-flight-area-expert"
```

技能目录位置：

- **Windows**：`C:\Users\<用户名>\.workbuddy\skills\`
- **macOS / Linux**：`~/.workbuddy/skills/`

> 安装后**重启 WorkBuddy 会话**，技能即出现在技能列表中。更新用 `git pull`。

## 💬 使用示例

在 WorkBuddy 中 @ 本技能后提问：

- `SMGCS 是什么`
- `道基强度的高强度对应的 E 值是多少`（MH5001）
- `4.12.2 跑道等待位置怎么设`（MH5001）
- `跑道道面错台多少要立即暂停起降`（CCAR-139B）
- `不停航施工怎么报批`（CCAR-139B）
- `修订案覆盖哪些条款`

## 📥 知识库如何扩充

「一个技能、多份规定」——新增规定只需往 `kb/` 加模块：

1. 在 `kb/<类别>/<规定>/` 新建模块（`MODULE.md` + `chapters/` + `source.txt`）
2. 在 `index/by-doc.md`、`index/by-topic.md` 补登记
3. 在 `SKILL.md` 的「模块地图」与「路由索引」补一行
4. 若为**版本更新**：另需**全局搜索并更新失效引用**（旧条款 / 旧术语）

类别目录：`01-法律法规` / `02-民航规章CCAR` / `03-行业标准MH` / `04-咨询通告AC` / `05-ICAO`

## ⚠️ 说明

- 本技能为**条款定位与汇总**，不替代规范正本；具体量值（几何尺寸、坡度、光强、阈值等）与正式设计/审定/处罚认定，以发布正本及主管部门解释为准。
- 内容来源为文本可提取 PDF 的条文；图（几何图、布置图）未收录。

## 📄 许可证

本项目以 [MIT 许可证](LICENSE) 开源。所整理的第三方标准 / 规章版权归原著作权人所有，本仓库仅作结构化整理，引用时请以规范正本为准。
