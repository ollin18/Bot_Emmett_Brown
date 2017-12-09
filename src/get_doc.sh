#!/usr/bin/env bash
# We need to download the file
wget http://www.dailyscript.com/scripts/bttf4th.pdf
# First we want to be able to convert the pdf to a txt
# many times the pdf have restricted this possibility
# so we decrypt it with the qpdf tool
qpdf --decrypt --password="" bttf4th.pdf backtothefuture.pdf

# Next we use the pdf2txt tool to convert the pdf to txt
pdf2txt backtothefuture.pdf > ../data/1_screen_play.txt

lynx --dump http://www.angelfire.com/tv2/seaQuestDSV2032/BTTF2.html > ../data/2_screen_play.txt
lynx --dump http://www.angelfire.com/tv2/seaQuestDSV2032/BTTF3.html > ../data/3_screen_play.txt

sed -n /^Doc:/,/^$/p ../data/1_screen_play.txt | sed s/Doc:'\s'//g | sed '/^\s*$/d' | tr '\n' ' ' > ../data/1_Doc.txt
sed -n /^Doc:/,/^$/p ../data/2_screen_play.txt | sed s/Doc:'\s'//g | sed '/^\s*$/d' | tr '\n' ' ' > ../data/2_Doc.txt
sed -n /^Doc:/,/^$/p ../data/3_screen_play.txt | sed s/Doc:'\s'//g | sed '/^\s*$/d' | tr '\n' ' ' > ../data/3_Doc.txt
cat ../data/1_Doc.txt ../data/2_Doc.txt ../data/3_Doc.txt > ../data/all_doc.txt
