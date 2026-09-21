# 民用机场飞行区技术标准 MH5001-2021

> 一个 WorkBuddy / Agent Skills 知识库，把《民用机场飞行区技术标准 MH 5001-2021》主文与**第一~第四修订案**整理为可检索、可问答的结构化知识。所有内容以修订案为准，被修正的原文标记为失效。

[![Standard](https://img.shields.io/badge/standard-MH%205001--2021-blue.svg)](#)
[![Amendments](https://img.shields.io/badge/amendments-1~4-green.svg)](#修订案覆盖)
[![Chapters](https://img.shields.io/badge/chapters-12-informational.svg)](#包含内容)

## 特性

- **修订案优先**：PCN/ACN → PCR/ACR、SMGCS、增强型滑行道中线等均以最新修订案为准
- **12 章结构化摘要**：从总则到标示障碍物的目视助航设施，逐章可定位
- **术语 / 流程 / 速查三件套**：`glossary` 术语表、`patterns` 评价流程、`cheatsheet` 决策规则
- **修订案权威登记**：`amendments.md` 逐条记录四份修订案覆盖的条款，便于溯源

## 包含内容

| 文件 | 内容 |
| --- | --- |
| `SKILL.md` | 技能入口：用法、核心框架、章节索引、主题索引、范围说明 |
| `chapters/ch01` ~ `ch12` | 12 章摘要（每章含 Amendment Notes） |
| `glossary.md` | 术语表（含 PCR/ACR、SMGCS 等修订后术语） |
| `patterns.md` | 评价流程（ACR-PCR 道面强度、跑道宽度判定等） |
| `cheatsheet.md` | 决策规则与阈值速查 |
| `amendments.md` | 四份修订案 clause-level 覆盖登记（权威依据） |

## 安装

把本文件夹（`mh5001-2021-flight-area-standard/`）复制到 WorkBuddy 技能目录：

- **Windows**：`C:\Users\<用户名>\.workbuddy\skills\`
- **macOS / Linux**：`~/.workbuddy/skills/`

```bash
git clone https://github.com/LazyRa/workbuddy-skills.git
cp -r workbuddy-skills/mh5001-2021-flight-area-standard "$HOME/.workbuddy/skills/"
```

重启 WorkBuddy 会话后，用中文直接提问即可。

## 使用示例

> 在 WorkBuddy 中 @ 本技能后提问：

- `SMGCS 是什么`
- `道基强度的高强度对应的 E 值是多少`
- `4.12.2 跑道等待位置怎么设`
- `ACR-PCR 怎么判`
- `修订案覆盖哪些条款`

## 修订案覆盖

| 修订案 | 覆盖要点 |
| --- | --- |
| 第一 | PCN/ACN → **PCR/ACR**；§3.6 整节重写（表 3.6.3 代号、超载规则） |
| 第二 | 新增 **1.0.4 SMGCS**、2.1.83 术语、2.3 缩略语（原 1.0.4 顺延 1.0.5） |
| 第三 | 表 3.6.3 道基强度 E 值改 ≥/< 区间；明确轻型航空器 ≤5700kg |
| 第四 | **4.12.2** 跑道等待位置；**6.2.8** 增强型滑行道中线；6.2.12 NO ENTRY；**8.4.7** 跑道脱离标记牌 |

## 说明

具体量值（跑道宽度、限制面坡度、灯光光强等）以正本条款及附录为准；本技能负责**条款定位与修订案追踪**，不替代规范正本的量值引用。

## 许可证

本技能整理文档以 [MIT](../../LICENSE) 许可证开源。所引用的《民用机场飞行区技术标准 MH 5001-2021》及其修订案版权归原著作权人所有，引用时请以规范正本为准。
