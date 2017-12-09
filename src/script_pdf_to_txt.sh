# We need to download the file
wget http://www.dailyscript.com/scripts/bttf4th.pdf
# First we want to be able to convert the pdf to a txt
# many times the pdf have restricted this possibility
# so we decrypt it with the qpdf tool
qpdf --decrypt --password="" bttf4th.pdf backtothefuture.pdf

# Next we use the pdf2txt tool to convert the pdf to txt
pdf2txt backtothefuture.pdf > 1_the_script.txt
