"""4-2 の解説図: 3つの処理のうち、違うのはフォーム・行き先・出力先の3か所だけ。

イメージスキーマ = PART-WHOLE（同じかたまりの中の、入れ替わる部分だけを取り出す）。
実行: cd images && python3 01-same-and-different.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

COLUMNS = [
    (260, "1. 資料検索", "blue", ["docsForm", "'docs.html?'", "docsResult"]),
    (500, "2. 全文検索", "green", ["fulltextForm", "'fulltext.html?'", "fulltextResult"]),
    (740, "3. 棚検索", "purple", ["shelfForm", "'shelf.html?'", "shelfResult"]),
]
ROWS = ["どのフォームか", "行き先", "どこに出すか"]

CELL_W = 230
ROW_H = 70
ROW_Y = [124, 214, 304]

c = Canvas(1010, 520)

c.text(505, 50, "3つの処理で違うのは、この3か所だけ", scale="heading", align="center")

for x, title, _color, _values in COLUMNS:
    c.text(x + CELL_W / 2, 104, title, scale="label", align="center")

for i, name in enumerate(ROWS):
    c.sticky(40, ROW_Y[i], 200, ROW_H, color="gray")
    c.text(140, ROW_Y[i] + 43, name, scale="label", align="center")

for x, _title, color, values in COLUMNS:
    for i, value in enumerate(values):
        c.sticky(x, ROW_Y[i], CELL_W, ROW_H, color=color)
        c.text(x + CELL_W / 2, ROW_Y[i] + 43, value, scale="label", align="center",
               font="technical")

c.sticky(40, 400, 930, 92, color="gray")
c.text(505, 436, "ここ以外は3つとも同じ", scale="label", align="center")
c.text(505, 468,
       "event.preventDefault()　new URLSearchParams()　"
       "new FormData(...).forEach(...)　createElement('a')",
       scale="caption", align="center", font="technical")

print(c.save("01-same-and-different.svg"))
