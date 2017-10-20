#!/bin/bash

echo "Content-type: text/html" #httpが解釈する場所、おまじない(あとで勉強)ー＞httpヘッダーにこれから書くのはhtmlで書かれたwebページだよって言ってる
echo
	echo "<table border ="1" align ="center">"
	     echo "<tr>"
	     	  echo "<th>"
	     	       echo "ID"
	     	  echo "</th>"
	     	  echo "<th>"
	     	       echo "title"
	          echo "</th>"
	   	  echo "<th>"
	     	       echo "author"
	     	  echo "</th>"
	     echo "</tr>"
cat target.txt | while IFS=',' read label title author image; #パイプを使って実装。標準入力じゃないから&ない
do
    if [ $label = "#ID" ]; then 
	continue #$label = "#ID"この時はその行を飛ばして次の繰り返しに移る(whileに移動)
    fi #finishではなくてifを単に逆にしたやつ
	echo "<tr>"
 	echo "<td>"
	     echo "<a href = "$image">"
	              echo "$label"
	     echo "</a>"
	     echo "</td>"
	     echo "<td>"
	     	  echo "$title"
	     echo "</td>"
	     echo "<td>"
	     	  echo "$author"
	     echo "</td>"
	echo "</tr>"
done

	echo "</table>"

