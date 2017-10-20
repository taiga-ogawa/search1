#!/bin/bash

source utils

echo "Content-type: text/html" #httpが解釈する場所、おまじない(あとで勉強)ー＞httpヘッダーにhtmlとして読み込ませる
echo

query=`cat` #``で囲むとコマンドの実行結果を変数に代入するようになる
echo '<meta http-equiv="Content-Type" content="text/html;charset=ISO-2022-JP"/>' #文字コードの設定、index.shtmlにあった
ID=`echo "$query" | lookup ID | decode` #queryを読み込んでlookup IDでIDの部分を取り出してdecode
title=`echo "$query" | lookup title | decode`
author=`echo "$query" | lookup author | decode`
url=`echo "$query" | lookup url | decode`

echo "$ID , $title , $author , $url" >> target.txt

echo "complete"
echo "<a href = "index.shtml">back"
echo "</a>"


