#!/usr/bin/env python3
"""Inline the Clinical Modern design tokens into the hub page and the faculty class report."""
import os
D = os.path.dirname(os.path.abspath(__file__))
t = open(os.path.join(D, "_tokens.css"), encoding="utf-8").read()
for src, out in (("src.html", "index.html"), ("report_src.html", "class-report.html")):
    s = open(os.path.join(D, src), encoding="utf-8").read()
    assert "/*@@TOKENS@@*/" in s, src
    open(os.path.join(D, out), "w", encoding="utf-8").write(s.replace("/*@@TOKENS@@*/", t))
    print("wrote", out)
