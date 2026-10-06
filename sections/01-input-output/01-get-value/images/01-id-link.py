"""1-1 の解説図: HTML の id 属性と getElementById の引数が同じ文字列で対応する。

イメージスキーマ = LINK（離れた2か所が1つの値で結ばれる）。
実行: cd images && python3 01-id-link.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(900, 300)

html = c.sticky(40, 70, 320, 120, color="blue")
c.text(200, 108, "HTML", scale="heading", align="center")
c.text(200, 150, '<input id="myInput" />', scale="body", align="center",
       font="technical")
c.text(200, 176, "id 属性", scale="caption", align="center")

js = c.sticky(540, 70, 320, 120, color="green")
c.text(700, 108, "JavaScript", scale="heading", align="center")
c.text(700, 150, "getElementById('myInput')", scale="body", align="center",
       font="technical")
c.text(700, 176, "引数", scale="caption", align="center")

key = c.sticky(395, 98, 110, 64, color="yellow")
c.text(450, 138, "myInput", scale="label", align="center", font="technical")

c.link(html, key)
c.link(key, js)

c.text(450, 255,
       "同じ文字列であることだけが、2つを対応づけている（違えば null が返る）",
       scale="body", align="center")

print(c.save("01-id-link.svg"))
