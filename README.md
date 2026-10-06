---
docs: true
title: URL生成ページを作るハンズオン
---

# URL生成ページを作るハンズオン

入力欄に値を入れて「生成」を押すと検索用の URL ができる、というページを 1 枚作ります。
HTML と JavaScript だけで作るので、ビルドもインストールも要りません。

必要なものは **サクラエディタ** と **Microsoft Edge** の 2 つだけです。

## 作るもの

先に完成形を触ってみてください。項目を埋めて「生成」を押すと、検索用の URL ができます。
できた URL はそのままクリックして開けます。

::preview[4つの章を終えたときの完成形]{src="04-multiple-forms/02-third-form" height="560"}

いまは何をしているか分からなくて構いません。これを4つの章に分けて、1つずつ作っていきます。

## 進め方

教材は 2 階層で整理されています。

- **章（セクション）** — テーマで束ねた親ディレクトリ（`sections/01-input-output/` など）
- **節（レクチャー）** — 1 回分の作業単位＝1 つの完成した `index.html`（`sections/01-input-output/01-get-value/` など）

各節の `example/index.html` がその時点の完成形です。Edge でダブルクリックして開けば動きます。
節の進め方は `LECTURE.md` に書いてあります。

第1章から第3章までは 1 枚の `index.html` を育て続け、第4章で同じ画面にフォームを足して仕上げます。

## 章の構成

| 章 | 内容 |
|---|---|
| [第1章 IDを使った入力と出力](./sections/01-input-output/01-get-value/LECTURE.md) | `getElementById` で値を取り、画面に出す |
| [第2章 文字列結合でURLを作る](./sections/02-build-url/01-one-param/LECTURE.md) | `?` と `&` を自分でつないで URL を組み立てる |
| [第3章 よりよく書く](./sections/03-better/01-url-search-params/LECTURE.md) | `URLSearchParams` / `createElement` / `form` の `submit` / `FormData` に置き換える |
| [第4章 1つの画面に複数のフォームを並べる](./sections/04-multiple-forms/01-second-form/LECTURE.md) | 行き先の違うフォームを3つ並べて仕上げる |

## 始め方

1. このリポジトリをクローンするか、ZIP でダウンロードする
2. [開発ツール（サクラエディタ / Edge）](./sections/TOOLS.md) をそろえる
3. [sections/README.md](./sections/README.md) の一覧から第1章の最初の節に進む

## ドキュメントサイト

各節の解説は GitHub Pages でも読めます: <https://seekseep.github.io/url-generator-handson/>

サイト上では、各ページの下にその場で触れるライブプレビューと完成コードが付いています。

## 題材について

架空の社内資料検索システムを題材にしています。行き先の URL（`docs.html` など）も
パラメータ名（`dept`、`title` など）も仮のものです。実際の案件で使うときは、
その検索システムのものに差し替えてください。

## ライセンス・注意事項

- 学習用リポジトリです
