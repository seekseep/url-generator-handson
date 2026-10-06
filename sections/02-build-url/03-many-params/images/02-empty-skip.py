"""2-3 の解説図: 空欄をそのままつなぐ場合と、飛ばす場合の違い。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(900, 340)

c.text(50, 50, "そのまま全部つなぐ", scale="heading", align="left")
bad = c.sticky(50, 72, 800, 70, color="red")
c.text(450, 116, "docs.html?dept=25&title=&author=&date=", scale="heading",
       align="center", font="technical")
c.text(450, 170, "空の値がそのまま並ぶ。受け取り側には「空文字で検索せよ」と伝わる",
       scale="body", align="center")

c.text(50, 240, "入力されたものだけつなぐ", scale="heading", align="left")
good = c.sticky(50, 262, 800, 70, color="green")
c.text(450, 306, "docs.html?dept=25", scale="heading", align="center",
       font="technical")

print(c.save("02-empty-skip.svg"))
