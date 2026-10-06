"""2-3 の解説図: 「?」は先頭の1回だけ、「&」は2つ目以降。

イメージスキーマ = PART-WHOLE（1本の文字列が区切りで分かれている）。
実行: cd images && python3 01-separators.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

PARTS = [
    ("docs.html", 180, "blue", None),
    ("?", 54, "orange", "先頭の1回だけ"),
    ("dept=25", 150, "green", None),
    ("&", 54, "orange", "2つ目以降"),
    ("title=月次報告", 230, "green", None),
    ("&", 54, "orange", "2つ目以降"),
    ("author=山田", 180, "green", None),
]

MARGIN = 40
GAP = 4
width = MARGIN * 2 + sum(w for _, w, _, _ in PARTS) + GAP * (len(PARTS) - 1)

c = Canvas(width, 250)
c.text(width / 2, 48, "区切り文字は位置によって変わる", scale="heading", align="center")

x = MARGIN
for label, w, color, note in PARTS:
    c.sticky(x, 92, w, 72, color=color)
    c.text(x + w / 2, 136, label, scale="body", align="center", font="technical")
    if note:
        c.text(x + w / 2, 200, note, scale="label", align="center")
    x += w + GAP

print(c.save("01-separators.svg"))
