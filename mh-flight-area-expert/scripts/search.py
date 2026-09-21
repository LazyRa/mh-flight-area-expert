#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""知识库全文 / 条款号检索。

用法:
  python search.py <关键词>
  python search.py 第47条
  python search.py 不停航施工
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent


def main():
    if len(sys.argv) < 2:
        print("用法: python search.py <关键词>")
        return
    kw = sys.argv[1]
    hits = 0
    for p in sorted(ROOT.rglob("*.md")):
        try:
            lines = p.read_text(encoding="utf-8").splitlines()
        except Exception:
            continue
        for i, ln in enumerate(lines, 1):
            if kw in ln:
                rel = p.relative_to(ROOT)
                print("%s:%d: %s" % (rel, i, ln.strip()[:120]))
                hits += 1
    print("\n共 %d 条命中" % hits)


if __name__ == "__main__":
    main()
