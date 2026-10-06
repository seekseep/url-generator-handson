"""3-4 の解説図: id と name は役割が違う。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(900, 330)

inp = c.sticky(300, 50, 300, 72, color="yellow")
c.text(450, 94, '<input id="dept" name="dept">', scale="body", align="center",
       font="technical")

idbox = c.sticky(60, 200, 340, 90, color="blue")
c.text(230, 238, "id", scale="heading", align="center", font="technical")
c.text(230, 270, "label の for と結びつける", scale="label", align="center")

namebox = c.sticky(500, 200, 340, 90, color="green")
c.text(670, 238, "name", scale="heading", align="center", font="technical")
c.text(670, 270, "送るときのキーになる", scale="label", align="center")

c.link(inp, idbox, primary=False)
c.link(inp, namebox, primary=False)

c.text(450, 160, "同じ文字列を書いているが、使われ方は別", scale="body",
       align="center")

print(c.save("01-name-vs-id.svg"))
