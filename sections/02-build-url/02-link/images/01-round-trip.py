"""2-2 の解説図: 作る側のページと受け取る側のページの関係。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 320)

maker = c.node(160, 120, "index.html", emoji_cp="1f310", w=180, h=92)
c.text(160, 200, "URL を作る側", scale="caption", align="center")

recv = c.node(700, 120, "docs.html", emoji_cp="1f5a5", w=180, h=92)
c.text(700, 200, "URL を受け取る側", scale="caption", align="center")

c.link(maker, recv, label="?title=月次報告")

out = c.sticky(560, 235, 280, 60, color="yellow")
c.text(700, 272, "title = 月次報告", scale="label", align="center", font="technical")
c.link(recv, out, primary=False)

c.text(160, 272, "2つは別々のファイル", scale="body", align="center")

print(c.save("01-round-trip.svg"))
