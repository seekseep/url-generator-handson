"""3-3 の解説図: form の既定動作を止めて、自分の処理に差し替える。"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(900, 400)

c.text(50, 54, "何も書かないとき", scale="heading", align="left")
a1 = c.node(190, 136, "submit", emoji_cp="1f4dd", w=160, h=92)
a2 = c.node(640, 136, "ページが読み込み直される", shape="sticky", color="red",
            w=300, h=92)
c.link(a1, a2, label="ブラウザの既定の動作")

c.text(50, 266, "preventDefault() を呼ぶとき", scale="heading", align="left")
b1 = c.node(190, 340, "submit", emoji_cp="1f4dd", w=160, h=92)
b2 = c.node(640, 340, "自分で URL を作る", shape="sticky", color="green",
            w=300, h=92)
c.link(b1, b2, label="既定の動作を止めてから")

print(c.save("01-prevent-default.svg"))
