"""4-1 の解説図: id はページ全体で1つ、name はフォームごとに同じ文字列でよい。

イメージスキーマ = CONTAINER（id が効く範囲はページ全体、name が効く範囲はフォーム）。
実行: cd images && python3 01-id-scope.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(1060, 360)

c.text(530, 50, "同じ「部署コード」の欄を2つ置くとき", scale="heading", align="center")

c.text(325, 104, "1. 資料検索", scale="label", align="center")
c.text(595, 104, "2. 全文検索", scale="label", align="center")

# id の行 — 2つのフォームで別の文字列にする。
c.sticky(40, 124, 140, 70, color="gray")
c.text(110, 167, "id", scale="heading", align="center", font="technical")

c.sticky(200, 124, 250, 70, color="blue")
c.text(325, 167, "docs-dept", scale="label", align="center", font="technical")

c.sticky(470, 124, 250, 70, color="green")
c.text(595, 167, "fulltext-dept", scale="label", align="center", font="technical")

c.text(748, 152, "ページ全体で1つだけ", scale="body", align="left")
c.text(748, 178, "重ねると先に出てきた方だけが返る", scale="caption", align="left")

# name の行 — どちらも同じ文字列のまま。
c.sticky(40, 224, 140, 70, color="gray")
c.text(110, 267, "name", scale="heading", align="center", font="technical")

c.sticky(200, 224, 250, 70, color="yellow")
c.text(325, 267, "dept", scale="label", align="center", font="technical")

c.sticky(470, 224, 250, 70, color="yellow")
c.text(595, 267, "dept", scale="label", align="center", font="technical")

c.text(748, 252, "フォームごとに同じでよい", scale="body", align="left")
c.text(748, 278, "受け取り側が待っている名前", scale="caption", align="left")

print(c.save("01-id-scope.svg"))
