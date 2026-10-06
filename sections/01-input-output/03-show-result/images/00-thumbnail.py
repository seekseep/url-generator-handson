"""1-3 のサムネ: 出力先が Console から画面に変わる。

イメージスキーマ = SOURCE-PATH-GOAL（着点が差し替わる）。
実行: cd images && python3 00-thumbnail.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 240)

btn = c.node(140, 110, "ボタンを押す", emoji_cp="1f5b1", w=160, h=92)   # 🖱️
js = c.node(450, 110, "登録した処理", emoji_cp="2699", w=150, h=92)     # ⚙️
scr = c.node(760, 110, "画面", emoji_cp="1f310", w=150, h=92)           # 🌐

c.link(btn, js, label="click")
c.link(js, scr, label="textContent")

c.text(440, 205, "Console ではなく、ページの上に値を出す", scale="body", align="center")

print(c.save("00-thumbnail.svg"))
