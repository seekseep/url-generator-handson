"""3-1 の解説図: URLSearchParams が引き受けてくれる3つのこと。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(900, 400)

jobs = [
    ("「?」と「&」の使い分け", 60),
    ("記号や日本語の変換", 155),
    ("キーと値の連結", 250),
]
nodes = []
for label, y in jobs:
    s = c.sticky(40, y, 280, 70, color="red")
    c.text(180, y + 43, label, scale="label", align="center")
    nodes.append(s)

tool = c.node(500, 155, "URLSearchParams", shape="hexagon", color="blue",
              w=230, h=130)

out = c.sticky(680, 120, 190, 70, color="green")
c.text(775, 162, "1本の文字列", scale="label", align="center")

for n in nodes:
    c.link(n, tool, primary=False)
c.link(tool, out)

c.text(450, 372, "自分で書くのは「キーと値を足すこと」だけになる", scale="body",
       align="center")

print(c.save("01-what-it-does.svg"))
