#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""民航规章入库助手 — 机械步骤自动化（配合 SKILL.md 使用）

职责：PDF 文本提取与清洗、初始化知识库骨架、建模块目录、生成 MODULE.md 骨架、
     登记索引、更新时归档旧版。智能结构化由 Agent 按 SKILL.md 完成。

用法:
  python ingest.py init    [--kb <知识库根>]
  python ingest.py extract <pdf> [-o out.txt]
  python ingest.py add     <pdf> --category <类别> --doc-no <文号> --title <名称> [--effective 日期] [--status 现行] [--slug slug]
  python ingest.py update  <pdf> --slug <slug> [--effective 日期] [--note 说明]
通用参数: --kb <知识库技能根> 覆盖 ingest.config.json

依赖: pypdf 或 pdfminer.six（有其一即可）
"""
import argparse
import datetime
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
CONFIG_PATH = HERE.parent / "ingest.config.json"

DEFAULT_CATEGORIES = ["01-法律法规", "02-民航规章CCAR", "03-行业标准MH", "04-咨询通告AC", "05-ICAO"]

INDEX_BY_DOC_HEAD = "# 文档清单 by-doc\n\n| 文号 | 名称 | 类别 | 状态 | 模块路径 |\n|---|---|---|---|---|\n"
INDEX_BY_TOPIC_HEAD = "# 主题索引 by-topic\n\n| 主题 | 规定 | 条款 | 模块 |\n|---|---|---|---|\n"

SKILL_PLACEHOLDER = """---
name: 民航飞行区专家
description: "民航飞行区运行规章知识库（多规定合集）。覆盖跑道/滑行道/机坪、标志灯光标记牌、障碍物限制面、道面强度、运行安全管理等。当提问涉及民用机场飞行区设计、运行、维护、合规时使用。"
---

# 民航飞行区专家（知识库）

> 由 regulation-ingest 初始化，请按需补全「专家人设 / 模块地图 / 路由索引」。

## 模块地图

| 类别 | 规定 | 状态 |
|---|---|---|
| （待收录） | | |

## 回答规范

- 先定位 -> 引原文 -> 判现行版本 -> 给结论 -> 超范围明说
- 必引条款号；区分现行/失效
"""

MODULE_TMPL = """# {title}

- **文号**：{doc_no}
- **类别**：{category}
- **发布/实施**：{effective}
- **状态**：{status}
- **入库日期**：{today}
- **源文件**：{src}

## 覆盖范围
（待补：该规定涵盖的飞行区运行主题）

## 章节目录
（待补：chapters/ 文件清单）

## 交叉引用
（待补：与其他规定/条款的引用关系）

## 关键条款索引
（待补：高频条款号 -> 一句话）

## 版本历史
- {today} 首次入库（{src}）
"""


def load_config():
    cfg = {
        "kb_root": r"C:\Users\wangd\.workbuddy\skills\mh-flight-area-expert",
        "repo_root": r"D:\github\workbuddy-skills",
        "categories": DEFAULT_CATEGORIES,
        "use_ocr_if_empty": False,
    }
    if CONFIG_PATH.exists():
        try:
            cfg.update(json.loads(CONFIG_PATH.read_text(encoding="utf-8")))
        except Exception as e:
            print("[warn] 读取 config 失败，用默认值: %s" % e, file=sys.stderr)
    return cfg


def write(path, content):
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    # 用 write_bytes 写纯 LF，避开 Windows write_text 自动转 CRLF 的坑
    path.write_bytes(content.encode("utf-8"))


def sanitize(text):
    if not text:
        return ""
    text = text.encode("utf-8", "ignore").decode("utf-8")  # 丢弃代理字符
    text = text.replace("\U001001b0", ".")                  # MH5001 PDF 里的全角句点字形
    return text.replace("\r\n", "\n").replace("\r", "\n")


def extract_pdf(path):
    text = ""
    try:
        from pypdf import PdfReader
        text = "\n".join((pg.extract_text() or "") for pg in PdfReader(str(path)).pages)
    except Exception:
        text = ""
    if not text.strip():
        try:
            from pdfminer.high_level import extract_text as pm_extract
            text = pm_extract(str(path))
        except Exception:
            text = ""
    return sanitize(text)


def slugify(text):
    s = re.sub(r"[^\w\-]+", "-", text, flags=re.UNICODE).strip("-").lower()
    return (s or "doc")[:80]


def find_module(kb_root, slug):
    base = Path(kb_root) / "kb"
    if not base.exists():
        return None
    for cat in base.iterdir():
        if cat.is_dir() and (cat / slug).is_dir():
            return cat / slug
    return None


def cmd_init(a, cfg):
    kb = Path(a.kb or cfg["kb_root"])
    (kb / "kb").mkdir(parents=True, exist_ok=True)
    for c in cfg["categories"]:
        (kb / "kb" / c).mkdir(parents=True, exist_ok=True)
    (kb / "index").mkdir(parents=True, exist_ok=True)
    (kb / "scripts").mkdir(parents=True, exist_ok=True)
    if not (kb / "index" / "by-doc.md").exists():
        write(kb / "index" / "by-doc.md", INDEX_BY_DOC_HEAD)
    if not (kb / "index" / "by-topic.md").exists():
        write(kb / "index" / "by-topic.md", INDEX_BY_TOPIC_HEAD)
    if not (kb / "SKILL.md").exists():
        write(kb / "SKILL.md", SKILL_PLACEHOLDER)
    if not (kb / "glossary.md").exists():
        write(kb / "glossary.md", "# 知识库术语表（跨规定）\n\n")
    print("[ok] 知识库骨架已就绪: %s" % kb)


def cmd_extract(a):
    t = extract_pdf(Path(a.pdf))
    if a.out:
        write(Path(a.out), t)
        print("[ok] 提取 %d 字符 -> %s" % (len(t), a.out))
    else:
        sys.stdout.write(t)
    if len(t.strip()) < 200:
        print("[warn] 文本极少，可能是扫描件，需要 OCR（本脚本不内置 OCR）", file=sys.stderr)


def cmd_add(a, cfg):
    kb = Path(a.kb or cfg["kb_root"])
    if not kb.exists():
        sys.exit("[error] 知识库根不存在: %s（先运行 init，或用 --kb 指定）" % kb)
    slug = a.slug or slugify(a.title)
    mod = kb / "kb" / a.category / slug
    if mod.exists() and not a.force:
        sys.exit("[error] 模块已存在: %s（若为更新请用 update，或加 --force）" % mod)
    text = extract_pdf(Path(a.pdf))
    write(mod / "source.txt", text)
    (mod / "chapters").mkdir(parents=True, exist_ok=True)
    write(mod / "MODULE.md", MODULE_TMPL.format(
        title=a.title, doc_no=a.doc_no, category=a.category,
        effective=a.effective or "待补", status=a.status,
        today=datetime.date.today().isoformat(), src=Path(a.pdf).name))
    idx = kb / "index" / "by-doc.md"
    if not idx.exists():
        write(idx, INDEX_BY_DOC_HEAD)
    with idx.open("a", encoding="utf-8", newline="\n") as f:
        f.write("| %s | %s | %s | %s | kb/%s/%s/ |\n" % (a.doc_no, a.title, a.category, a.status, a.category, slug))
    print("[ok] 模块: %s" % mod)
    print("[ok] source.txt（%d 字符）+ MODULE.md 骨架 + index/by-doc.md 已登记" % len(text))
    print("[next] Agent 待办：切分 chapters/、补全 MODULE.md、更新 by-topic/glossary/SKILL、安全扫描、push")


def cmd_update(a, cfg):
    kb = Path(a.kb or cfg["kb_root"])
    mod = find_module(kb, a.slug)
    if not mod:
        sys.exit("[error] 找不到模块 slug=%s" % a.slug)
    today = datetime.date.today().isoformat()
    src = mod / "source.txt"
    if src.exists():
        hist = mod / "history"
        hist.mkdir(exist_ok=True)
        src.replace(hist / ("source-%s.txt" % today))
    text = extract_pdf(Path(a.pdf))
    write(src, text)
    amd = mod / "amendments.md"
    if not amd.exists():
        write(amd, "# 修订登记 — %s\n" % a.slug)
    with amd.open("a", encoding="utf-8", newline="\n") as f:
        f.write("\n## %s 更新（%s）\n- 变更说明：%s\n- 生效日期：%s\n- [ ] 受影响条款：待补\n- [ ] 失效原文：待补\n"
                % (today, Path(a.pdf).name, a.note or "待补", a.effective or "待补"))
    print("[ok] 更新模块: %s" % mod)
    print("[ok] 旧版归档 history/，新 source.txt 已写入（%d 字符），amendments.md 已追加" % len(text))
    print("[next] 必做：① MODULE.md 标注失效/修订；② 全局搜索 KB 内旧条款/旧术语引用并更新；③ 安全扫描；④ push")


def main():
    ap = argparse.ArgumentParser(description="民航规章入库助手")
    sub = ap.add_subparsers(dest="cmd", required=True)

    pi = sub.add_parser("init"); pi.add_argument("--kb", default="")
    pe = sub.add_parser("extract"); pe.add_argument("pdf"); pe.add_argument("-o", "--out")

    pa = sub.add_parser("add")
    pa.add_argument("pdf")
    pa.add_argument("--category", required=True)
    pa.add_argument("--doc-no", required=True)
    pa.add_argument("--title", required=True)
    pa.add_argument("--effective", default="")
    pa.add_argument("--status", default="现行")
    pa.add_argument("--slug", default="")
    pa.add_argument("--kb", default="")
    pa.add_argument("--force", action="store_true")

    pu = sub.add_parser("update")
    pu.add_argument("pdf")
    pu.add_argument("--slug", required=True)
    pu.add_argument("--effective", default="")
    pu.add_argument("--note", default="")
    pu.add_argument("--kb", default="")

    a = ap.parse_args()
    cfg = load_config()

    if a.cmd == "init":
        cmd_init(a, cfg)
    elif a.cmd == "extract":
        cmd_extract(a)
    elif a.cmd == "add":
        cmd_add(a, cfg)
    elif a.cmd == "update":
        cmd_update(a, cfg)


if __name__ == "__main__":
    main()
