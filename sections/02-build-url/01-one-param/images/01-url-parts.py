"""2-1 の解説図: URL を「行き先」「?」「キー=値」に分解する。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(900, 300)

base = c.sticky(50, 90, 230, 80, color="blue")
c.text(165, 138, "docs.html", scale="heading", align="center", font="technical")
c.text(165, 205, "行き先のページ", scale="label", align="center")

mark = c.sticky(300, 90, 70, 80, color="gray")
c.text(335, 140, "?", scale="title", align="center", font="technical")
c.text(335, 205, "区切り", scale="label", align="center")

kv = c.sticky(390, 90, 460, 80, color="green")
c.text(620, 138, "title=月次報告", scale="heading", align="center", font="technical")
c.text(500, 205, "キー", scale="label", align="center")
c.text(740, 205, "値", scale="label", align="center")
c.text(500, 232, "検索システムが決めている", scale="caption", align="center")
c.text(740, 232, "入力された文字", scale="caption", align="center")

c.text(450, 45, "この3つをつなげた1本の文字列が URL になる", scale="heading", align="center")

print(c.save("01-url-parts.svg"))
