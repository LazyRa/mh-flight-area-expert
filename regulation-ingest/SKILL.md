---
name: 民航规章入库助手
description: "把新的民航规章/标准 PDF 自动提取、清洗、结构化，并入「民航飞行区专家」知识库（mh-flight-area-expert）。支持新增（add）与版本更新（update）两种流程。当用户丢来一份规章 PDF 要求入库/加入知识库，或说明这是某规定的更新版本时使用。"
---

# 民航规章入库助手（regulation-ingest）

把一份 PDF 规章 → 结构化模块 → 并入飞行区专家知识库。
**Agent 按本文件执行；机械步骤调用 `scripts/ingest.py`。**

## 目标知识库

| 项 | 路径 |
|---|---|
| 知识库技能根（live） | `C:\Users\wangd\.workbuddy\skills\mh-flight-area-expert` |
| 仓库镜像（GitHub 工作副本） | `D:\github\workbuddy-skills` |
| 配置 | `ingest.config.json` |
| Python（含 pypdf/pdfminer） | `C:\Users\wangd\.workbuddy\binaries\python\envs\default\Scripts\python.exe` |

> 知识库根不存在时，先运行 `python scripts/ingest.py init` 生成骨架。

## 触发判定

- 用户给 PDF + "入库 / 加入知识库" → **新增流程（add）**
- 用户给 PDF + "这是更新 / 新版本" → **更新流程（update）**
- 拿不准 → **先问用户**（新增还是更新、文号、类别）

## 新增流程（add）

1. **确认元数据**（缺就问，别编）：`文号` · `名称` · `类别`(01-法律法规 / 02-民航规章CCAR / 03-行业标准MH / 04-咨询通告AC / 05-ICAO) · `发布日期` · `状态`
2. **提取清洗**：`python scripts/ingest.py extract <pdf> -o <tmp>`；字符数 <200 → 提示可能扫描件需 OCR，**停下告知用户**。
3. **建模块**：`python scripts/ingest.py add <pdf> --category <类别> --doc-no <文号> --title <名称> --effective <日期>`
   → 生成 `kb/<类别>/<slug>/`（含 `source.txt`、`chapters/`、`MODULE.md` 骨架）并登记 `index/by-doc.md`。
4. **切分章节**（Agent 判断）：读 `source.txt`，按"章/条"切 `chapters/*.md`，每条给 Core Idea / Key Clauses / 交叉引用。
5. **补全 `MODULE.md`**：覆盖范围、章节目录、交叉引用、关键条款索引。
6. **挂总索引**：`index/by-topic.md` 加主题映射；知识库级 `glossary.md` 补术语；知识库级 `SKILL.md` 模块地图补一行。
7. **安全扫描**：`python C:\Users\wangd\.workbuddy\skills\book-to-skill\tools\scan_generated_skill.py <知识库根>`
8. **同步仓库**：知识库根内容同步到 `D:\github\workbuddy-skills\mh-flight-area-expert\` → `git add/commit/push`。

## 更新流程（update）

1. 确认被更新的 `slug`、新版日期、变更说明。
2. 提取清洗（同 add 第 2 步）。
3. 入库：`python scripts/ingest.py update <pdf> --slug <slug> --effective <日期> --note "<变更说明>"`
   → 旧 `source.txt` 移入 `history/`，写新 `source.txt`，追加 `amendments.md` 条目骨架。
4. **标注失效**：`MODULE.md` 把被覆盖条款标 `[失效]`，新条款标 `[修订]`。
5. **全局搜失效引用**（最容易漏，别跳）：grep 整个知识库，找引用旧条款 / 旧术语的地方并更新（`index/by-topic.md`、`glossary.md`、其他模块）。
6. 安全扫描 + 同步仓库（同 add 第 7/8 步）。

## 自检清单

- [ ] MODULE.md 元数据完整（文号 / 状态 / 日期）
- [ ] source.txt 字符数正常（非扫描件）
- [ ] chapters/ 已切分且可定位
- [ ] index/by-doc.md 已登记
- [ ] index/by-topic.md 已映射
- [ ] 更新时：失效引用已全局搜索
- [ ] 安全扫描通过
- [ ] 仓库已 push

## 知识库骨架（`init` 生成）

```
mh-flight-area-expert/
├── SKILL.md            # 专家人设 + 模块地图 + 路由索引
├── index/
│   ├── by-doc.md
│   └── by-topic.md
├── kb/
│   01-法律法规/ 02-民航规章CCAR/ 03-行业标准MH/ 04-咨询通告AC/ 05-ICAO/
├── glossary.md         # 跨规定术语表
└── scripts/
```

## 边界

- 不编造元数据；来源合法性由用户确认。
- 扫描件（无文本层）需 OCR，当前脚本不内置 OCR，遇此停下告知用户。
- 智能结构化（切章、填内容、写交叉引用）是 Agent 的活，脚本只做机械部分。
