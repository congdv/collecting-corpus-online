from urllib import urlopen
from bs4 import BeautifulSoup
from bs4 import SoupStrainer
import io 

#@param url page container sentence pairs
def main(url):

	#parsing only tr tag of document
	only_tr_tags = SoupStrainer("tr")

	# innit soup
	soup = BeautifulSoup(urlopen(url), "html.parser", parse_only = only_tr_tags)

	#find all tr tag
	for td in soup.find_all("td"):
		f.write(td.get_text() + '\n')
def get_link(url):
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    links = bsObj.findAll("span",attrs={"class":"field-content"})
    for link in links: 
         print(link.find("a"))
def get_link_tag(url):
    link_list =[]
    link_url = "http://tiengtrungnet.com" 
    html = urlopen(url)
    bsObj = BeautifulSoup(html)
    links = bsObj.find("div",{"id":"content"}).findAll("a",{"class":"imagecache"})
    for link in links:
        if 'href' in link.attrs:
            link_list.append(link_url+link.attrs['href'])
    return link_list
def get_all_link():
    url = "http://tiengtrungnet.com/tai-lieu-hoc-tieng-trung/tu-vung"
    link_collection = get_link_tag(url)
    url_page = url +"?page="
    for i in range(1,21):
        url = url_page +"%d"%i
        link_collection.append(get_link_tag(url))
    return link_collection

#link_list = get_all_link()
#for link in link_list:
#    print link+"\n"
if __name__ == "__main__":

    #init out put filename path
    filename = 'Output.txt'

    #open file in write mode, encoding = utf-8
    f = io.open(filename, 'w', encoding='utf-8')
    check = True
    url = "http://tiengtrungnet.com/tai-lieu-hoc-tieng-trung/tu-vung"
    i = 1
    if check is True:
        for link in get_link_tag(url):
            main(link)
            f.write(u'\n')
            print "Trang %d"%i
            i = i + 1
        check = False
    if check is False:
        for i in range(1,21):
            url_temp = url+"?page=%d"%i
            for link in get_link_tag(url_temp):
                main(link)
                f.write(u'\n')
                print "Trang %d"%i
                i = i + 1
    f.close()

