# 3-3 フォームの submit を使う

URL生成ページを作るハンズオン の 1 レクチャー。ビルド・パッケージ管理なしで、ブラウザだけで動きます。

## 構成

```text
03-form-submit/
├── LECTURE.md        教材本文（docs: true → サイトに載る）
├── README.md         このファイル
├── images/           説明図の SVG（00-thumbnail.svg を先頭サムネに）
├── example/          動くコード ← 配布 ZIP とライブプレビューの元
│   ├── docs.html       資料検索の受け取り側（同梱）
│   └── index.html      学習者が書くファイル
└── demos/            解説用デモ（ZIP には入らない）
    └── no-prevent-default/index.html
```

## 動かす

`example/index.html` を Edge で開くだけです。画像や音を読み込まないので、
エクスプローラーからダブルクリックしても動きます。

編集はサクラエディタで行います。保存するときは文字コードを **UTF-8** にしてください。
