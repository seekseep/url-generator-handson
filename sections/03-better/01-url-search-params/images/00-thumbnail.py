"""3-1 のサムネ: 自前の分岐を URLSearchParams に置き換える。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 250)

before = c.sticky(40, 80, 240, 80, color="red")
c.text(160, 115, "自分で書く", scale="label", align="center")
c.text(160, 143, "if が8個", scale="body", align="center")

tool = c.node(450, 120, "URLSearchParams", emoji_cp="2699", w=200, h=92)

after = c.sticky(640, 80, 210, 80, color="green")
c.text(745, 115, "任せる", scale="label", align="center")
c.text(745, 143, "append するだけ", scale="body", align="center")

c.link(before, tool)
c.link(tool, after)

c.text(440, 215, "動きは変えずに、組み立てをブラウザの道具に渡す", scale="body",
       align="center")

print(c.save("00-thumbnail.svg"))
