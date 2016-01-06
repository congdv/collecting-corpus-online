from urllib.request import urlopen
from bs4 import BeautifulSoup
import os.path
import io

#filename path store for write
file_name = 'output.txt'
f = io.open(file_name,'w',encoding='utf-16')
#initialize page number
page_num = 1
#Address page will parse
def get_url(link,num_page,extension):
    url = link + str(num_page) + extension
    return url
# Get max page in vietgle website
"""
def find_max_page(link):
   first_page = urlopen(link)
   page_bsObj = BeautifulSoup(first_page)
   num_page = page_bsObj.find("div",{"id":"ctl00_ContentPlaceHolderMain_paging"})
   if num_page is None:
       return "Not found"
#   for page in num_page:
#       print (page.get_text())
#        return "Found it"
   return num_page 
"""
#function store date to file_name
#@param:bsObj content html
def write_file(bsObj):
    for child in bsObj.findAll("ul",{"class":"uccss"}):
        chinese_str = child.find("li",{"class":"ctk"}).get_text()
        vietnamese_str = child.find("li",{"class":"p10l"}).get_text()
        f.write(chinese_str+'\n')
        f.write(vietnamese_str+'\n')

#initialize attribute about url
link = "http://tratu.coviet.vn/hoc-tieng-trung/cap-cau-song-ngu/vietgle-tra-tu/tat-ca/trang-"
extension = ".html"
#write total page to file
for i in range(1,3425):
    url = get_url(link,i,extension)
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    write_file(bsObj)
