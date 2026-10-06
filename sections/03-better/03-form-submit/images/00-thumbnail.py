"""3-3 のサムネ: click から form の submit に変える。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 300)

btn = c.node(150, 120, "ボタンを押す", emoji_cp="1f5b1", w=170, h=92)
enter = c.sticky(40, 198, 220, 48, color="gray")
c.text(150, 230, "入力欄で Enter", scale="label", align="center")

form = c.node(500, 140, "form の submit", emoji_cp="1f4dd", w=190, h=92)
js = c.sticky(700, 102, 160, 76, color="green")
c.text(780, 148, "URL を作る", scale="label", align="center")

c.link(btn, form)
c.link(enter, form, primary=False)
c.link(form, js)

c.text(440, 275, "click だけでなく、入力欄での Enter でも同じ処理が動く", scale="body",
       align="center")

print(c.save("00-thumbnail.svg"))
