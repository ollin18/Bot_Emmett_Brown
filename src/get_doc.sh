sed -n /^Doc:/,/^$/p ../data/1_screen_play.txt | sed s/Doc:'\s'//g | sed '/^\s*$/d' | tr '\n' ' ' > ../data/1_Doc.txt
sed -n /^Doc:/,/^$/p ../data/2_screen_play.txt | sed s/Doc:'\s'//g | sed '/^\s*$/d' | tr '\n' ' ' > ../data/2_Doc.txt
sed -n /^Doc:/,/^$/p ../data/3_screen_play.txt | sed s/Doc:'\s'//g | sed '/^\s*$/d' | tr '\n' ' ' > ../data/3_Doc.txt
cat ../data/1_Doc.txt ../data/2_Doc.txt ../data/3_Doc.txt > ../data/all_doc.txt
