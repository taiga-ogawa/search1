#!/bin/bash
source utils
echo "Content-type: text/html" #httpが解釈する場所、おまじない(あとで勉強)ー＞httpヘッダーにこれから書くのはhtmlで書かれたwebページだよって言ってる
echo
	echo "<table border ="1" align ="center">"
	     echo "<tr>"
	     	  echo "<th>"
	     	       echo "検索結果"
	     	  echo "</th>"
		  echo "<th>"
	     	       echo "類似度"
	          echo "</th>"
	   	  echo "<th>"
	     	       echo "title"
	     	  echo "</th>"
		  echo "<th>"
		       echo "author"
		  echo "</th>"
		  echo "</tr>"
label=`echo $QUERY_STRING | lookup id | decode` #QUERY_STRINGは環境変数だから大文字、これでurlの部分持って来れる。
# http://www.coins.tsukuba.ac.jp/~s1511353/search/result.cgi?id=Image5のid=Image5をgetリクエストでゲット。
# sim.txtを読むー＞grepでクリックした画像のrgbを出力ー＞while readでrgbを格納ー＞sim.txtを読むー＞今回は全ての画像の内積だからgrepで指定しない、そうすると全部出力ー＞rgbを変数に格納ー＞labelと内積を同じ行に書いていくー＞sort
cat sim.txt | grep "$label" | while read _ a b c; #パイプの後のreadを単体で使うと変数を持ち越せない！grepは入力に対して、指定した文字列を含む行を返す
do
    cat sim.txt | while read label d e f;
    do
	echo "$label" `echo $a $b $c $d $e $f | ./naiseki` #``で囲むことでechoに二つ引数を与えられる
    done | sort -nk2r | while read Image sim;# -nk2で昇順、逆順はrをつけるといい
    do	echo "<tr>"
	echo "<td>"
	echo "$Image"
	echo "</td>"
	echo "<td>"
	echo $sim
	echo "</td>"
	cat target.txt | grep $Image | while IFS=',' read label title author image;
	do
	echo "<td>"
	echo "$title"
	echo "</td>"
	echo "<td>"
	echo "$author"
	echo "</td>"
	done
	echo "</tr>"
    done
done
echo "</table>"
