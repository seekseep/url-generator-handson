"""1-3 の解説図: 同じ文字列でも textContent と innerHTML で結果が変わる。

イメージスキーマ = SPLITTING（同じ入力が2つの扱いに分岐する）。
実行: cd images && python3 02-text-vs-html.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(900, 380)

src = c.sticky(40, 140, 250, 100, color="yellow")
c.text(165, 180, "入力された文字", scale="label", align="center")
c.text(165, 215, "<b>太字</b>", scale="body", align="center", font="technical")

keep = c.sticky(590, 50, 280, 100, color="green")
c.text(730, 90, "文字として置く", scale="label", align="center")
c.text(730, 125, "<b>太字</b>", scale="body", align="center", font="technical")

parse = c.sticky(590, 230, 280, 100, color="red")
c.text(730, 270, "タグとして解釈する", scale="label", align="center")
c.text(730, 307, "太字", scale="title", align="center")

c.link(src, keep, label="textContent")
c.link(src, parse, label="innerHTML")

print(c.save("02-text-vs-html.svg"))
