"""3-4 のサムネ: 入力欄ごとに取り出すのをやめ、FormData でまとめて取る。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 260)

before = c.sticky(40, 85, 270, 86, color="red")
c.text(175, 120, "入力欄ごとに取り出す", scale="label", align="center")
c.text(175, 150, "getElementById × 4", scale="caption", align="center",
       font="technical")

tool = c.node(470, 128, "FormData", emoji_cp="1f4e6", w=160, h=92)

after = c.sticky(650, 85, 200, 86, color="green")
c.text(750, 120, "まとめて取る", scale="label", align="center")
c.text(750, 150, "1回で全部", scale="caption", align="center")

c.link(before, tool)
c.link(tool, after)

c.text(440, 225, "入力欄が増えても、取り出す処理は増えない", scale="body",
       align="center")

print(c.save("00-thumbnail.svg"))
