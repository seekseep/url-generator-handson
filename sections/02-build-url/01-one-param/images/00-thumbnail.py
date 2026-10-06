"""2-1 のサムネ: 入力値を文字列結合して URL にする。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 240)

inp = c.node(130, 110, "入力欄", emoji_cp="1f4dd", w=150, h=92)
js = c.node(420, 110, "文字列結合", emoji_cp="2699", w=150, h=92)
url = c.sticky(610, 72, 250, 76, color="green")
c.text(735, 118, "docs.html?title=…", scale="label", align="center", font="technical")

c.link(inp, js, label=".value")
c.link(js, url)

c.text(440, 205, "ベースURL に「?」とキー=値をつないで、検索用のURLを作る",
       scale="body", align="center")

print(c.save("00-thumbnail.svg"))
