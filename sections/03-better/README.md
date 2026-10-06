---
docs: true
title: よりよく書く
sidebar:
  label: 章のはじめに
  order: 0
---

# 第3章 よりよく書く

できあがったものの動きは変えず、書き方だけを直していきます。
第2章で自分で面倒を見ていたことを、ブラウザが元から持っている道具に渡していく章です。

| 第2章の書き方 | この章での書き方 |
|---|---|
| `'?' + 'dept=' + 値 + '&' + ...` | `URLSearchParams` |
| `'<a href="' + url + '">'` | `createElement` ＋ `setAttribute` |
| ボタンの `click` ＋ `alert` で必須チェック | `form` の `submit` ＋ `required` |
| 入力欄ごとに `getElementById` | `FormData` |

どれも「自分で書いた文字列の組み立てをやめる」という同じ方向の変更です。

## この章のレクチャー

1. [URLSearchParams に置き換える](./01-url-search-params/LECTURE.md) — `?` と `&` の分岐をなくす
2. [リンクを要素として作る](./02-create-link/LECTURE.md) — `createElement` と `setAttribute`
3. [フォームの submit を使う](./03-form-submit/LECTURE.md) — Enter キー、`required`、`preventDefault`
4. [FormData でまとめて取り出す](./04-form-data/LECTURE.md) — `name` 属性で一括取得
