"""1-2 のサムネ: ボタンを押したときだけ処理が走る。

イメージスキーマ = SOURCE-PATH-GOAL（押す→動く→出る）。
実行: cd images && python3 00-thumbnail.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 240)

btn = c.node(140, 110, "ボタンを押す", emoji_cp="1f5b1", w=160, h=92)   # 🖱️
js = c.node(450, 110, "登録した処理", emoji_cp="2699", w=150, h=92)     # ⚙️
con = c.node(760, 110, "Console", shape="sticky", color="gray", w=180, h=92)

c.link(btn, js, label="click")
c.link(js, con, label="そのときの値")

c.text(440, 205, "押すたびに、そのときの入力値を読み直す", scale="body", align="center")

print(c.save("00-thumbnail.svg"))
