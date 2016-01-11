import urllib
import time
import urllib2
from bs4 import BeautifulSoup
import io
import webbrowser
import requests

def main(wordList):
    i = 1
    for word in wordList:
    #start infor mation about a word
        f.write(u"-----Start word------\n")
        #content process
        #get content that request to website
        try:
            the_page = getResponseFromPostMethod('E',word)
        #handle error request forbidden
        except urllib2.HTTPError as error:
            print error
            return None
        #use lib for parse html struct
        soup = BeautifulSoup(the_page)
        #get title page
        if soup.find('title').get_text()=='YellowBridge Human User Verification':
            webbrowser.open_new_tab('http://www.yellowbridge.com/general/captcha.php')
            time.sleep(10)
            the_page = getResponseFromPostMethod('E',word)
            soup = BeautifulSoup(the_page)
		
        print word
        #find all tr tag, get text with '|' separator
        try:
	    tabletag = soup.find('table', {'id':'multiRow'})
            for trtag in tabletag.find_all('tr'):
	        f.write(trtag.get_text('|') + '\n')
                print 'In tu'+trtag.get_text()
        except AttributeError as error:
            print "not found html tag because forbidden"
            #url = 'http://www.yellowbridge.com/chinese/dictionary.php' 

            #webbrowser.open_new_tab(url)
        #end infomation about a word
        f.write(u"-----End word-------\n")
        print i
        i = i + 1

def getResponseFromPostMethod(searchMode, word):
	
    #destination page exploit
    url = 'http://www.yellowbridge.com/chinese/dictionary.php'

    # user_agent get from http://www.useragentstring.com/
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'

    #value is param send in post method
    # values = {'searchMode' : 'E',
    #           'word' : 'hello'
    #          }
    values = {'searchMode' : searchMode,
              'word' : word
             }
    cookies = '_ga=GA1.2.133163078.1451881386; PHPSESSID=rfaq4drk716uj9cgbppp7aijl7; _gat=1'
    #header of request
    headers = { 'User-Agent' : user_agent,'Cookie':cookies}
    #encode url(values)
    data = urllib.urlencode(values)
    #create request
    req = urllib2.Request(url, data, headers)
    #get response
    response = urllib2.urlopen(req)
        
    return response


    
if __name__ == '__main__':

    #demo with 10 word in wordlist
    #wordList = ['hello', 'class', 'friend', 'orange', 'address', 'alone', 'answer', 'box', 'bicycle', 'field']
    #initialize wordList variable
    wordList = []
    #read vocabulary from file word_list_english.txt
    word_list_file = open('word_list_english.txt','r')
    for line in word_list_file:
        wordList.append(line.rstrip())
    #close file word_list_english.txt
    word_list_file.close()
    filename = 'output.txt'
    f = io.open(filename, 'w', encoding='utf-8')
    #collect chinese - english word
    main(wordList)
    #close collective file
    f.close()


