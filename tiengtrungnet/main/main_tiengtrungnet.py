#import
import os.path
from urllib import urlopen
from bs4 import BeautifulSoup
import io
from bs4 import SoupStrainer


#@param url page container sentence pairs
def main(url):

	#parsing only tr tag of document
	only_tr_tags = SoupStrainer("tr")

	# innit soup
	soup = BeautifulSoup(urlopen(url), "html.parser", parse_only = only_tr_tags)

	#find all tr tag
	for td in soup.find_all("td"):
		f.write(td.get_text() + '\n')

#get list link tiengtrungnet
def getListLinkSiteTiengTrungNet():

	url = "http://tiengtrungnet.com/tong-hop-list-tu-vung-tieng-trung"

	soup = BeautifulSoup(urlopen(url))

	myList1 = []
	for child in soup.find_all("div", class_ = "content clearfix"):
		for ptag in child.find_all("p"):
			link = ptag.find("a", {"target":"_blank"})
			if link != None:
				myList1.append(link.get('href'))

	myList2 = []
	for i in range(4,124):
		myList2.append(myList1[i])

	return myList2


if __name__ == "__main__":

	#init out put filename path
	filename = 'Output5.txt'

	#open file in write mode, encoding = utf-8
	f = io.open(filename, 'w', encoding='utf-8')
	myListLink = getListLinkSiteTiengTrungNet()
	i = 0
	for link in myListLink:
		i = i + 1;
		print("Dang get trang %d"%i)
		main(link)
		f.write('\n')
	f.close()

