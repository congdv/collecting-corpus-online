#import
import os.path
from urllib import urlopen
from bs4 import BeautifulSoup
import io


url = "http://tratu.coviet.vn/hoc-tieng-trung/cap-cau-song-ngu/vietgle-tra-tu/tat-ca/trang-1.html"
html = urlopen(url)
soup = BeautifulSoup(html)

for child in soup("ul", class_ = "uccss"):
	print(child.find("li", class_ = "ctk").string)
	print(child.find("li", class_ = "p10l").string)
