---
docs: true
title: IDを使った入力と出力
sidebar:
  label: 章のはじめに
  order: 0
---

# 第1章 IDを使った入力と出力

入力欄に書いた文字を JavaScript で受け取り、画面に出すところまでをやります。
URL はまだ作りません。「HTML の要素に `id` を付けて、JavaScript から `getElementById` で取る」
というこの章のやり方が、残りの章すべての土台になります。

出発点はこれだけです。

```html
<input id="myInput" />
<script>
  const myInput = document.getElementById('myInput');
  console.log(myInput.value);
</script>
```

## この章のレクチャー

1. [入力した値を取り出す](./01-get-value/LECTURE.md) — `getElementById` と `.value`、Console で確かめる
2. [ボタンを押したときに取り出す](./02-on-click/LECTURE.md) — `addEventListener` でクリックを受ける
3. [画面に表示する](./03-show-result/LECTURE.md) — `textContent` で出力先に書き込む
