import urllib
import time
import urllib2
from bs4 import BeautifulSoup
import io

def main(wordList):
    i = 1
    for word in wordList:
    #start infor mation about a word
        f.write(u"-----Start word------\n")
        #content process
        time.sleep(5)
        the_page = getResponseFromPostMethod('E',word)
        print the_page.read()
        soup = BeautifulSoup(the_page)
		
        print word
        #find all tr tag, get text with '|' separator
        try:
	    tabletag = soup.find('table', {'id':'multiRow'})
            for trtag in tabletag.find_all('tr'):
	        f.write(trtag.get_text('|') + '\n')
                print 'In tu'+trtag.get_text()
        except AttributeError as error:
            f.write(word.decode('utf-8') + '\n')
            print error
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

    #header of request
    headers = { 'User-Agent' : user_agent }
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
    wordList = []
    word_list_file = open('word_list_english.txt','r')
    for line in word_list_file:
        wordList.append(line.rstrip())
    word_list_file.close()
    filename = 'output.txt'
    f = io.open(filename, 'w', encoding='utf-8')
    main(wordList)
    f.close()


