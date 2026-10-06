"""1-1 の解説図: 取り出した入力欄から `.value` で中の文字を取る。

イメージスキーマ = CONTAINER（入れ物の中身を取り出す）。
実行: cd images && python3 02-value.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(860, 260)

el = c.node(160, 120, "input 要素", emoji_cp="1f4dd", w=150, h=92)  # 📝

box = c.sticky(560, 80, 260, 86, color="yellow")
c.text(690, 135, "月次報告", scale="title", align="center")

c.link(el, box, label=".value")

c.text(160, 205, "型・幅・入力中の文字などを持つ", scale="caption", align="center")
c.text(690, 205, "入力された文字列だけ", scale="caption", align="center")

print(c.save("02-value.svg"))
