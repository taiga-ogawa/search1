#!/bin/bash
echo "Content-type: text/html" #httpが解釈する場所、おまじない(あとで勉強)ー＞httpヘッダーにこれから書くのはhtmlで書かれたwebページだよって言ってる
echo

cat target.txt | while IFS=',' read label title author image; #パイプを使って実装。標準入力じゃないから&ない
do
    if [ $label = "#ID" ]; then 
	continue #$label = "#ID"この時はその行を飛ばして次の繰り返しに移る(whileに移動)
    fi #finishではなくてifを単に逆にしたやつ
	     echo "<a href = "result.cgi?id=$label">"
	     echo "<img src="$image">"
	     echo "</a>"
done
