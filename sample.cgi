#!/bin/bash
source utils
query=`cat`
echo "Content-type: text/html" #httpが解釈する場所、おまじない(あとで勉強)ー＞httpヘッダーにこれから書くのはhtmlで書かれたwebページだよって言ってる
echo
value=`echo "$query" | lookup KEYWORD | decode` #標準入力の時だけ&必要、区切り文字の変更
echo $value |./search.pl | while IFS=',' read label title author image; #パイプを使って実装。標準入力じゃないから&ない
do echo "<img src='$image'>"
echo "<HR>" #htmlを書けるのは単にブラウザが解釈するから
echo "title:$title" #変数を使う時は""で囲むダブルクォーテーション！！！！
echo "<br>" #""付けないとリダイレクトでエラー
echo "author:$author"
done

