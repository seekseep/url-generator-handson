"""2-4 のサムネ: 必須項目が空なら URL を作らずに止める。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 250)

empty = c.sticky(40, 80, 220, 76, color="gray")
c.text(150, 126, "dept が空", scale="label", align="center", font="technical")

stop = c.node(450, 118, "alert で止める", emoji_cp="26a0", w=180, h=92)
url = c.sticky(650, 80, 200, 76, color="gray")
c.text(750, 126, "URL は作らない", scale="label", align="center")

c.link(empty, stop)
c.link(stop, url, label="return", dash="dashed", primary=False)

c.text(440, 215, "検索システムが必須にしている項目は、作る前に確かめる",
       scale="body", align="center")

print(c.save("00-thumbnail.svg"))
