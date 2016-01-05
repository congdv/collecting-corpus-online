from urllib.request import urlopen
from bs4 import BeautifulSoup
html = urlopen("http://tratu.coviet.vn/hoc-tieng-trung/cap-cau-song-ngu/vietgle-tra-tu/tat-ca/trang-1.html")
bsObj = BeautifulSoup(html)
for child in bsObj.findAll("ul",{"class":"uccss"}):
    print (child.find("li",{"class":"ctk"}).get_text())
    print (child.find("li",{"class":"p10l"}).get_text())
