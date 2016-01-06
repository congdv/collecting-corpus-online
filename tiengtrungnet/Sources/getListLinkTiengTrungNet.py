#import
import os.path
from urllib import urlopen
from bs4 import BeautifulSoup
import io
from bs4 import SoupStrainer


url = "http://tiengtrungnet.com/tong-hop-list-tu-vung-tieng-trung"

soup = BeautifulSoup(urlopen(url))

myList1 = []
for child in soup.find_all("div", class_ = "content clearfix"):
	for ptag in child.find_all("p"):
		link = ptag.find("a", {"target":"_blank"})
		if link != None:
			# print(link.get('href'))
			myList1.append(link.get('href'))

myList2 = []
for i in range(4,124):
	myList2.append(myList1[i])

for link in myList2:
	print(link)