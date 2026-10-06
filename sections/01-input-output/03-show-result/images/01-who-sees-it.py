"""1-3 の解説図: Console は作る人しか見ない。画面は使う人に届く。

イメージスキーマ = SPLITTING（届く先が2つに分かれる）。
実行: cd images && python3 01-who-sees-it.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(860, 420)

dev = c.node(170, 110, "作る人", emoji_cp="1f464", w=150, h=92)         # 👤
con = c.node(640, 110, "Console", shape="sticky", color="gray", w=220, h=92)
c.link(dev, con, label="F12 で開く")

user = c.node(170, 280, "使う人", emoji_cp="1f464", w=150, h=92)        # 👤
scr = c.node(640, 280, "画面", emoji_cp="1f310", w=150, h=92)           # 🌐
c.link(user, scr, label="開けば見える")

c.text(430, 395, "Console に出している限り、使う人には何も届かない",
       scale="body", align="center")

print(c.save("01-who-sees-it.svg"))
