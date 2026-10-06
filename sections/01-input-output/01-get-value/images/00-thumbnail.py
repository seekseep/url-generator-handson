"""1-1 のサムネ: 入力欄 → JavaScript → Console という一方向の流れ。

イメージスキーマ = SOURCE-PATH-GOAL（起点→経路→着点）。
実行: cd images && python3 00-thumbnail.py
"""

import pathlib
import sys

sys.path.insert(0, str(pathlib.Path.home() / ".claude/skills/genfig"))
from genfig import Canvas  # noqa: E402

c = Canvas(880, 240)

inp = c.node(130, 110, "入力欄", emoji_cp="1f4dd")       # 📝
js = c.node(440, 110, "JavaScript", emoji_cp="2699")     # ⚙️
con = c.node(750, 110, "Console", shape="sticky", color="gray", w=190, h=92)

c.link(inp, js, label="id で呼ぶ")
c.link(js, con, label="console.log")

c.text(440, 205, "入力した文字を受け取って、開発者ツールに出すところから始める",
       scale="body", align="center")

print(c.save("00-thumbnail.svg"))
