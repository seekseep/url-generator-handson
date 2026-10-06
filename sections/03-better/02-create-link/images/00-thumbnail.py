"""3-2 のサムネ: タグを文字列で組み立てるのをやめ、要素として作る。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 250)

before = c.sticky(40, 80, 280, 80, color="red")
c.text(180, 115, "文字列でタグを書く", scale="label", align="center")
c.text(180, 145, "'<a href=\"' + url + '\">'", scale="caption", align="center",
       font="technical")

after = c.sticky(560, 80, 290, 80, color="green")
c.text(705, 115, "要素として作る", scale="label", align="center")
c.text(705, 145, "createElement('a')", scale="caption", align="center",
       font="technical")

c.link(before, after, label="書き換え")

c.text(440, 215, "タグの文字列を自分で組み立てない", scale="body", align="center")

print(c.save("00-thumbnail.svg"))
