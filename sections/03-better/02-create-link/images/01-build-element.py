"""3-2 の解説図: 要素を作って画面に入れるまでの4ステップ。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(960, 300)

steps = [
    ("createElement('a')", "a 要素を作る", "blue"),
    ("setAttribute(...)", "href と target を付ける", "blue"),
    ("textContent = url", "表示する文字を入れる", "blue"),
    ("append(link)", "画面に入れる", "green"),
]

prev = None
x = 40
for code, note, color in steps:
    s = c.sticky(x, 100, 200, 80, color=color)
    c.text(x + 100, 146, code, scale="caption", align="center", font="technical")
    c.text(x + 100, 212, note, scale="caption", align="center")
    if prev is not None:
        c.link(prev, s)
    prev = s
    x += 230

c.text(480, 55, "作る → 属性を付ける → 文字を入れる → 画面に入れる", scale="heading",
       align="center")
c.text(480, 262, "append するまで、作った要素は画面に出ない", scale="body",
       align="center")

print(c.save("01-build-element.svg"))
