---
name: 民用机场飞行区技术标准 MH5001-2021
description: "Knowledge base from 《民用机场飞行区技术标准 MH 5001-2021》主文 + 第一~第四修订案. Use when referencing flight-area planning/design (runway, taxiway, apron), obstacle limitation surfaces, visual aids (markings/lights/signs), pavement strength (ACR-PCR), SMGCS, or applying its mandatory clauses. All content reflects the four amendments — amended originals are void."
---

<!-- argument-hint: [topic, clause number, or chapter, e.g. ACR-PCR, 障碍物限制面, 4.12.2, ch03] -->

# 民用机场飞行区技术标准 MH5001-2021

**标准**：MH 5001-2021 ｜ **章节**：12 章 ｜ **修订案**：第一~第四（已并入，原文失效优先以修订案为准）｜ **Generated**：2026-09-21

## How to Use This Skill

- **Without arguments** — load core frameworks (below) for reference
- **With a topic** — ask about `ACR-PCR`、`障碍物限制面`、`SMGCS`、`跑道等待位置`；I find and read the relevant chapter
- **With a clause** — ask for `4.12.2` / `表3.6.3` / `8.4.7`；I load that exact clause context
- **With chapter** — ask for `ch03`；I load that chapter file
- **Browse** — ask "有哪些章节" to see the full index
- **Amendments** — ask `修订案` / `amendments`；I load the override register

When you ask about a topic not in Core Frameworks, I read the relevant chapter before answering. **All answers apply the four amendments; PCN/ACN and other amended originals are void.**

---

## Core Frameworks & Mental Models

**1. ACR-PCR 道面强度体系（第一+第三修订案）** — 取代旧 PCN/ACN。
- 可用判定：`ACR ≤ PCR` → 可用；`ACR > PCR` → 仅当同时满足：① 道面无破坏、道基未减弱；② 柔性 ≤110%、刚性 ≤105%（105–110% 刚性须专门评估）；③ 年超载 ≤ 年总运行 **5%**。
- 报告代号（表 3.6.3）：道面 R/F ｜ 道基 A(≥150)/B(100–150)/C(60–100)/D(<60 MPa) ｜ 胎压 W(无)/X(≤1.75)/Y(≤1.25)/Z(≤0.50) ｜ 评定 T/U。
- 轻型航空器 = 机坪质量 **≤5700kg**（仅报最大质量+胎压）。

**2. 飞行区两级指标** — 指标Ⅰ(1–4) 由基准飞行场地长度+翼展/主起落架外轮外边距定；指标Ⅱ(A–F) 由翼展+主起落架外轮外边距定。指标越高，几何与设施要求越严（查表 4.1.4/4.4.3/4.9.5）。

**3. 障碍物限制面设立（按跑道类型）** — 非仪表(内水平/锥形/进近/过渡) ⊂ 非精密进近(+内进近/复飞) ⊂ 精密进近(全部 8 类含内过渡)。限制面内物体必须标示（Ch 12）。

**4. 跑道等待位置设置（第四修订案 4.12.2）** — 滑行道(非单向出口)与跑道相交处设；仅出口滑行道仅 1 个；跑道交跑道处设。对应标志 6.2.10、标记牌 8.3/8.4.7。

**5. SMGCS 强制设置（第二修订案 1.0.4）** — 机场必须设置地面活动引导及控制系统；新增术语 2.1.83、缩略语 2.3。

**6. 助航灯光 = 一级负荷中特别重要负荷** — 双重电源+应急电源（表 10.1.6）；RVR<550m 须停止排灯；精密进近跑道须中线灯/接地带灯。

**7. 标志/标记牌第四修订案要点** — 增强型滑行道中线标志（每条滑行道接跑道处，除出口）；NO ENTRY 禁止进入标志（仅出口滑行道，白字红底，距 0.8–1.3W）；滑行边线标志与等待位置相交处中断净距 0.9m；跑道脱离标记牌设在等待位置处，ILS/MLS 时避让临界/敏感区。

---

## Chapter Index

| # | Title | Key Frameworks |
|---|-------|----------------|
| [ch01](chapters/ch01-总则.md) | 总则 | 指标Ⅰ/Ⅱ分级、SMGCS(新增1.0.4) |
| [ch02](chapters/ch02-术语与缩略语.md) | 术语、符号和缩略语 | PCR/ACR(改)、SMGCS(新增)、E |
| [ch03](chapters/ch03-航空数据与道面强度.md) | 航空数据与道面强度 | ACR-PCR 评价、表3.6.3、超载规则 |
| [ch04](chapters/ch04-跑道与滑行道及机坪.md) | 跑道、滑行道、机坪及附属设施 | 几何尺寸查表、RESA、4.12.2(改) |
| [ch05](chapters/ch05-障碍物限制面.md) | 障碍物限制面 | 8类限制面、按跑道类型设立 |
| [ch06](chapters/ch06-标志与标志物.md) | 标志与标志物 | 增强型中线、NO ENTRY(第四修订案) |
| [ch07](chapters/ch07-助航灯光.md) | 助航灯光 | 进近/PAPI/跑道/滑行道灯光 |
| [ch08](chapters/ch08-标记牌.md) | 标记牌 | 强制/信息牌、8.4.7(改) |
| [ch09](chapters/ch09-机坪助航设备.md) | 机坪助航设备 | 泛光照明、VDGS/高级VDGS |
| [ch10](chapters/ch10-目视助航设施供电系统.md) | 目视助航设施供电系统 | 特别重要负荷、TN-S/TT |
| [ch11](chapters/ch11-目视助航设施监视与控制系统.md) | 监视与控制系统 | 灯光监控、机坪设备监控 |
| [ch12](chapters/ch12-标示障碍物的目视助航设施.md) | 标示障碍物的目视助航设施 | 物体标志/灯光、附录J |

## Topic Index

- **ACR-PCR / 道面强度** → ch03, cheatsheet, amendments(第一/三)
- **PCR / ACR** → ch02, ch03（旧 PCN/ACN 失效）
- **SMGCS** → ch01(1.0.4), ch02(2.1.83/2.3), amendments(第二)
- **飞行区指标** → ch01, ch03, ch04
- **障碍物限制面** → ch05, ch12
- **跑道等待位置** → ch04(4.12.2), ch06(6.2.10), ch08(8.3)
- **增强型滑行道中线标志 / NO ENTRY** → ch06, amendments(第四)
- **跑道脱离标记牌** → ch08(8.4.7), amendments(第四)
- **助航灯光** → ch07, ch10
- **标记牌** → ch08
- **机坪 / VDGS** → ch09
- **供电 / 监控** → ch10, ch11
- **修订案覆盖** → amendments.md

## Supporting Files

- [glossary.md](glossary.md) — 关键术语（含 PCR/ACR、SMGCS、失效旧词警示）
- [patterns.md](patterns.md) — 7 个可复用评价/判定流程
- [cheatsheet.md](cheatsheet.md) — 决策规则与阈值速查
- [amendments.md](amendments.md) — 四份修订案 clause-level 覆盖登记（权威依据）

---

## Scope & Limits

本技能覆盖 MH 5001-2021 主文及第一~第四修订案的现行有效条文。四份修订案修改的条款以修订案为准，被修正的原文（含 PCN/ACN 体系、旧 1.0.4 编号、旧 6.2.8/8.4.7 表述）**已失效**，不得作为合规依据。

- 具体数值（跑道宽度、升降带宽度、限制面坡度/尺寸、灯光光强、障碍灯参数等）引用以源文 **表 4.1.4 / 4.4.3 / 4.9.5 / 5.2.7 / 10.1.6 / 附录 E/G/I/J** 为准，本技能提供条款定位而非替代原文量值。
- 本技能为知识索引/参考，不替代标准正本；正式设计/审定请以发布正本及主管部门解释为准。
- 源文件为文本可提取 PDF，无图片遗漏（文字层完整）。
