"""2-3 のサムネ: 4つの入力欄をつないで1本のクエリ文字列にする。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 260)

form = c.node(140, 120, "4つの入力欄", emoji_cp="1f4dd", w=170, h=92)
js = c.node(430, 120, "つなぐ", emoji_cp="2699", w=140, h=92)
url = c.sticky(600, 82, 260, 76, color="green")
c.text(730, 128, "dept=25&title=…", scale="label", align="center", font="technical")

c.link(form, js)
c.link(js, url, label="&")

c.text(440, 220, "入力されたものだけを「&」でつないでいく", scale="body", align="center")

print(c.save("00-thumbnail.svg"))
