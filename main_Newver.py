#import
from bs4 import SoupStrainer
from bs4 import BeautifulSoup
from urllib import urlopen
import io


def main(numPage):
	

	only_ul_tags = SoupStrainer("ul")
	url = str("http://tratu.coviet.vn/hoc-tieng-trung/cap-cau-song-ngu/vietgle-tra-tu/tat-ca/trang-%d.html"%numPage)
	soup = BeautifulSoup(urlopen(url), "html.parser", parse_only = only_ul_tags)
	
	for child in soup.select(".uccss"):
		f.write(child.find("li", class_ = "ctk").string + '\n')
		f.write(child.find("li", class_ = "p10l").string + '\n')

if __name__ == "__main__":

	filename = 'Output.txt'
	f = io.open(filename, 'w', encoding='utf-8')
	for numPage in range(1,3425):
		print ("Lay trang %d")%numPage
		main(numPage)

	f.close()