#import
from bs4 import SoupStrainer
from bs4 import BeautifulSoup
from urllib import urlopen
import io

#@param: numPage is order page
def main(numPage):

	#parsing only ul tag of document
	only_ul_tags = SoupStrainer("ul")

	#get url by numPage param
	url = str("http://tratu.coviet.vn/hoc-tieng-trung/cap-cau-song-ngu/vietgle-tra-tu/tat-ca/trang-%d.html"%numPage)

	# innit soup
	soup = BeautifulSoup(urlopen(url), "html.parser", parse_only = only_ul_tags)

	# for a uccss class
	for child in soup.select(".uccss"):

		#find and write a string of li class ctk - chinese sentence
		f.write(child.find("li", class_ = "ctk").string + '\n')

		#find and write a string of li class p10l - vietnamese sentence
		f.write(child.find("li", class_ = "p10l").string + '\n')


if __name__ == "__main__":

	#init out put filename path
	filename = 'Output.txt'

	#open file in write mode, encoding = utf-8
	f = io.open(filename, 'w', encoding='utf-8')

	#numPage range from 1 to 3425
	for numPage in range(1,3425):
		print ("Lay trang %d")%numPage
		main(numPage)
	f.close()