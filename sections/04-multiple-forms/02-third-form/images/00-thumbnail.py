"""4-2 のサムネ: 3つのフォームが並んだ完成形。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 400)

c.sticky(30, 40, 480, 330, color="gray")
c.text(70, 78, "index.html", scale="label", align="left", font="technical")

rows = [
    ("1. 資料検索", "docs.html", "blue", 100),
    ("2. 全文検索", "fulltext.html", "green", 196),
    ("3. 棚検索", "shelf.html", "purple", 292),
]
for title, dest, color, y in rows:
    f = c.sticky(60, y, 420, 72, color=color)
    c.text(270, y + 44, title, scale="heading", align="center")
    d = c.sticky(620, y, 230, 72, color=color)
    c.text(735, y + 44, dest, scale="label", align="center", font="technical")
    c.link(f, d)

print(c.save("00-thumbnail.svg"))
