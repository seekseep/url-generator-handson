"""4-1 のサムネ: 1つの画面に、行き先の違うフォームを2つ並べる。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 320)

page = c.sticky(30, 40, 480, 250, color="gray")
c.text(70, 78, "index.html", scale="label", align="left", font="technical")

f1 = c.sticky(60, 100, 420, 72, color="blue")
c.text(270, 144, "1. 資料検索", scale="heading", align="center")

f2 = c.sticky(60, 196, 420, 72, color="green")
c.text(270, 240, "2. 全文検索", scale="heading", align="center")

d1 = c.sticky(620, 100, 230, 72, color="blue")
c.text(735, 144, "docs.html", scale="label", align="center", font="technical")

d2 = c.sticky(620, 196, 230, 72, color="green")
c.text(735, 240, "fulltext.html", scale="label", align="center", font="technical")

c.link(f1, d1)
c.link(f2, d2)

print(c.save("00-thumbnail.svg"))
