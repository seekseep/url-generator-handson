"""2-2 のサムネ: 文字列だった URL をクリックできるリンクにする。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 240)

txt = c.sticky(40, 72, 230, 76, color="gray")
c.text(155, 118, "文字列のURL", scale="label", align="center")

link = c.node(450, 110, "リンク", emoji_cp="1f517", w=150, h=92)
page = c.node(760, 110, "docs.html", emoji_cp="1f5a5", w=170, h=92)

c.link(txt, link, label="innerHTML")
c.link(link, page, label="クリック")

c.text(440, 205, "コピーして貼り直さなくても、押せば開けるようにする",
       scale="body", align="center")

print(c.save("00-thumbnail.svg"))
