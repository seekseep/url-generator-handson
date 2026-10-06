---
docs: true
title: 進め方
sidebar:
  label: 進め方
  order: 0
---

# 進め方

入力欄に値を入れて「生成」を押すと検索用の URL ができる、というページを 1 枚作ります。
使うのは HTML と JavaScript だけです。ビルドもインストールも要りません。

## 進め方

教材は 2 階層になっています。

- **章（セクション）** — テーマで束ねたまとまり（`01-input-output/` など）
- **節（レクチャー）** — 1 回分の作業単位（`01-input-output/01-get-value/` など）

1 つの節につき、完成したファイルが `example/` に入っています。
サイト上では各ページの下に動くプレビューと完成コードが付いているので、
**自分で書いてみる → うまくいかなければ完成コードを見る** という順で進めてください。

第1章から第3章までは 1 枚の `index.html` を育て続けます。第4章でそこにフォームを足して仕上げます。
前の節のファイルをコピーして、その節の差分だけを足していく形です。

## セットアップ

- [開発ツール（サクラエディタ / Edge）](./TOOLS.md)

## 章の一覧

### [第1章 IDを使った入力と出力](./01-input-output/README.md)

1. [入力した値を取り出す](./01-input-output/01-get-value/LECTURE.md)
2. [ボタンを押したときに取り出す](./01-input-output/02-on-click/LECTURE.md)
3. [画面に表示する](./01-input-output/03-show-result/LECTURE.md)

### [第2章 文字列結合でURLを作る](./02-build-url/README.md)

1. [パラメータが1つのURLを作る](./02-build-url/01-one-param/LECTURE.md)
2. [生成したURLをリンクにする](./02-build-url/02-link/LECTURE.md)
3. [パラメータを増やす](./02-build-url/03-many-params/LECTURE.md)
4. [必須の項目をチェックする](./02-build-url/04-required/LECTURE.md)

### [第3章 よりよく書く](./03-better/README.md)

1. [URLSearchParams に置き換える](./03-better/01-url-search-params/LECTURE.md)
2. [リンクを要素として作る](./03-better/02-create-link/LECTURE.md)
3. [フォームの submit を使う](./03-better/03-form-submit/LECTURE.md)
4. [FormData でまとめて取り出す](./03-better/04-form-data/LECTURE.md)

### [第4章 1つの画面に複数のフォームを並べる](./04-multiple-forms/README.md)

1. [同じ画面に2つ目のフォームを足す](./04-multiple-forms/01-second-form/LECTURE.md)
2. [3つ目を足して仕上げる](./04-multiple-forms/02-third-form/LECTURE.md)

## 題材について

架空の社内資料検索システムを題材にしています。パラメータ名（`dept`、`title` など）も
参考値も仮のものです。実際の案件で使うときは、行き先の URL とパラメータ名を
その検索システムのものに差し替えてください。
