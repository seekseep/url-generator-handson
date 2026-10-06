"""2-4 の解説図: 値に「&」が入ると、受け取り側が別のパラメータとして読む。

イメージスキーマ = SPLITTING（1つの値が2つに割れてしまう）。
実行: cd images && python3 01-broken-chars.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(900, 420)

src = c.sticky(50, 50, 800, 68, color="yellow")
c.text(450, 92, "件名に  A&B社 報告  と入力した", scale="heading", align="center")

url = c.sticky(50, 196, 800, 68, color="red")
c.text(450, 238, "docs.html?title=A&B社 報告", scale="heading", align="center",
       font="technical")

left = c.sticky(140, 330, 290, 66, color="gray")
c.text(285, 371, "title = A", scale="label", align="center", font="technical")

right = c.sticky(470, 330, 290, 66, color="gray")
c.text(615, 371, "B社 報告 = （空）", scale="label", align="center", font="technical")

c.link(src, url, label="文字列結合")
c.link(url, left, primary=False)
c.link(url, right, primary=False)

c.text(450, 300, "受け取り側は「&」をパラメータの区切りとして読む", scale="body",
       align="center")

print(c.save("01-broken-chars.svg"))
