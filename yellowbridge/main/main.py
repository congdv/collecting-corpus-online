import urllib
import urllib2
from bs4 import BeautifulSoup
import io

def main(wordList):
	i = 0
	for word in wordList:
		i = i + 1
		print("Dang get tu thu %d"%i)

		#start infor mation about a word
    f.write(u"-----Start word------\n")

		#content process
		the_page = getResponseFromPostMethod('E', word).read()
		soup = BeautifulSoup(the_page)
		tabletag = soup.find('table', {'id':'multiRow'})

		#find all tr tag, get text with '|' separator
		for trtag in tabletag.find_all('tr'):
			f.write(trtag.get_text('|') + '\n')

		#end infomation about a word
    f.write(u"-----End word-------\n")


def getResponseFromPostMethod(searchMode, word):
	
	#destination page exploit
	url = 'http://www.yellowbridge.com/chinese/dictionary.php'

	# user_agent get from http://www.useragentstring.com/
	user_agent = 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.106 Safari/537.36'

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
	wordList = ['hello', 'class', 'friend', 'orange', 'address', 'alone', 'answer', 'box', 'bicycle', 'field']

	filename = 'yellowbridgeOutput.txt'
	f = io.open(filename, 'w', encoding='utf-8')
	main(wordList)
	f.close()