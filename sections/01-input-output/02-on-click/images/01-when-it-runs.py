"""1-2 の解説図: 「読み込んだ瞬間に1回だけ」と「押すたびに」の対比。

イメージスキーマ = SPLITTING（同じ流れが2通りに分かれる）＋ BLOCKAGE（上段は届かない）。
実行: cd images && python3 01-when-it-runs.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 420)

c.text(50, 54, "前の節：読み込んだ瞬間に1回だけ", scale="heading", align="left")
a1 = c.node(220, 140, "入力し直す", emoji_cp="1f4dd", w=160, h=92)      # 📝
a2 = c.node(660, 140, "Console", shape="sticky", color="gray", w=190, h=92)
c.link(a1, a2, label="何も起きない", dash="dashed", primary=False)

c.text(50, 264, "この節：押すたびに動く", scale="heading", align="left")
b1 = c.node(220, 340, "ボタンを押す", emoji_cp="1f5b1", w=160, h=92)    # 🖱️
b2 = c.node(660, 340, "Console", shape="sticky", color="green", w=190, h=92)
c.link(b1, b2, label="1行ずつ増える")

print(c.save("01-when-it-runs.svg"))
