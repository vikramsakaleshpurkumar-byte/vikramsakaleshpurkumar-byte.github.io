#!/usr/bin/env python3
"""Inline the Clinical Modern design tokens into the hub page."""
import os
D = os.path.dirname(os.path.abspath(__file__))
s = open(os.path.join(D, "src.html"), encoding="utf-8").read()
t = open(os.path.join(D, "_tokens.css"), encoding="utf-8").read()
assert "/*@@TOKENS@@*/" in s
open(os.path.join(D, "index.html"), "w", encoding="utf-8").write(s.replace("/*@@TOKENS@@*/", t))
print("wrote index.html")
