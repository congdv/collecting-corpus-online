import urllib
import time
import urllib2
from bs4 import BeautifulSoup
import io
import random
import os.path
from sys import argv

script, session_file, word_list_file, out_put_file = argv

def main(wordList,session_list):

    i = 1
    j = 0
    _len = len(session_list)

    #x init from 0
    for word in wordList:
        print i
        # delays for 5 seconds
        # time.sleep(5)

        # content process

        # get random user agent string in list
        # userAgentString = random.choice(User_agent_List)
        print session_list[j]
        try:
            the_page = getResponseFromPostMethod('E', word, session_list[j])
        except:
            print 'Error request'

        #parse html structure
        soup = BeautifulSoup(the_page.read())
        print 'Session %d'%j
        if soup.find('title').get_text() == 'YellowBridge Human User Verification':
            j = j + 1
            if j == _len:
                j = 0
            the_page = getResponseFromPostMethod('E',word,session_list[j])
            soup = BeautifulSoup(the_page.read())
            print 'False'
        print word
        # find all tr tag, get text with '|' separator
        try:
            tabletag = soup.find('table', {'id': 'multiRow'})
            if(tabletag != None):
                for trtag in tabletag.find_all('tr'):
                    f.write(trtag.get_text('|')+ u'\n')
                print 'OK'
            else:
                print 'Not Found ' + word 

        except AttributeError as error:
            print 'Not Found ' + error 
        i = i + 1
        if i == 10:
            break


def getResponseFromPostMethod(searchMode, word, session_id):

    # destination page exploit
    url = 'http://www.yellowbridge.com/chinese/dictionary.php'

    # user_agent get from http://www.useragentstring.com/
    user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:43.0) Gecko/20100101 Firefox/43.0'

    # value is param send in post method
    # values = {'searchMode' : 'E',
    #           'word' : 'hello'
    #          }
    values = {'searchMode': searchMode,
              'word': word
              }
    #cookie for request
    cookie = 'PHPSESSID=' + session_id
    # header of request
    headers = {'User-Agent': user_agent, 'Cookie':cookie}
    # encode url(values)
    data = urllib.urlencode(values)
    # create request
    req = urllib2.Request(url, data, headers)
    # get response
    response = urllib2.urlopen(req)
    return response


if __name__ == '__main__':

    # demo with 10 word in wordlist
    # wordList = ['hello', 'class', 'friend', 'orange', 'address', 'alone', 'answer', 'box', 'bicycle', 'field']
    
    #initialize session list variable
    session_list = []
    #read session collection
    sessions = open(session_file,'r')
    for session in sessions:
        session_list.append(session.rstrip('\n'))

    # initialize wordList variable
    wordList = []

    # read vocabulary from file word_list_english.txt
    word_list_file = open(word_list_file, 'r')
    for line in word_list_file:
        wordList.append(line.rstrip())

    # close file word_list_english.txt
    word_list_file.close()

    filename = out_put_file

    #check filename is existed
    if os.path.isfile(filename):
        f = io.open(filename, 'a', encoding='utf-8')
    else:
        f = io.open(filename, 'w', encoding='utf-8')

    # collect chinese - english word
    main(wordList,session_list)

    # close collective file
    f.close()
