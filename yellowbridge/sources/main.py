import urllib
import time
import urllib2
from bs4 import BeautifulSoup
import io
import random
import os.path



def main(wordList):

    User_agent_List = ['Mozilla/5.0 (compatible; U; ABrowse 0.6; Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
                       'Mozilla/5.0 (compatible; U; ABrowse 0.6;  Syllable) AppleWebKit/420+ (KHTML, like Gecko)',
                       'Mozilla/5.0 (compatible; ABrowse 0.4; Syllable)',
                       'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR 3.5.30729)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0;   Acoo Browser; GTB5; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1;   SV1) ; InfoPath.1; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
                       'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; Trident/4.0; Acoo Browser 1.98.744; .NET CLR   3.5.30729)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; America Online Browser 1.1; Windows NT 5.1; (R1 1.5); .NET CLR 2.0.50727; InfoPath.1)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; America Online Browser 1.1; rev1.5; Windows NT 5.1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
                       'AmigaVoyager/3.2 (AmigaOS/MC680x0)',
                       'AmigaVoyager/2.95 (compatible; MC680x0; AmigaOS; SV1)',
                       'Mozilla/5.0 (compatible; MSIE 9.0; AOL 9.7; AOLBuild 4343.19; Windows NT 6.1; WOW64; Trident/5.0; FunWebProducts)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.27; Windows NT 5.1; Trident/4.0; .NET CLR 2.0.50727; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; AOL 9.7; AOLBuild 4343.21; Windows NT 5.1; Trident/4.0; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; .NET CLR 3.0.04506.648; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET4.0C; .NET4.0E)',
                       'Mozilla/5.0 (X11; U; UNICOS lcLinux; en-US) Gecko/20140730 (KHTML, like Gecko, Safari/419.3) Arora/0.8.0',
                       'Mozilla/5.0 (X11; U; Linux; de-DE) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3)  Arora/0.8.0',
                       'Mozilla/5.0 (X11; U; Linux; ru-RU) AppleWebKit/527+ (KHTML, like Gecko, Safari/419.3)  Arora/0.6 (Change: 802 025a17d)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; Avant Browser; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0)',
                       'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0; GTB6.4; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; chromeframe; Avant Browser; .NET CLR 1.1.4322; .NET CLR 2.0.50727; .NET CLR 3.0.04506.30; InfoPath.1; .NET CLR 3.0.4506.',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; Avant Browser; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30618)',
                       'Mozilla/5.0 (Windows; U; WinNT; en; rv:1.0.2) Gecko/20030311 Beonex/0.8.2-stable',
                       'Mozilla/5.0 (Windows; U; WinNT; en; Preview) Gecko/20020603 Beonex/0.8-stable',
                       'Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)',
                       'Mozilla/5.0 (X11; U; Linux x86_64; en-GB; rv:1.8.1b1) Gecko/20060601 BonEcho/2.0b1 (Ubuntu-edgy)',
                       'Mozilla/5.0 (X11; U; Linux i686; nl; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2 (Debian-1.99+2.0b2+dfsg-1)',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.8.1b2) Gecko/20060821 BonEcho/2.0b2',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1a3) Gecko/20060526 BonEcho/2.0a3',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1b2) Gecko/20060826 BonEcho/2.0b2',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.8.1.8pre) Gecko/20071012 BonEcho/2.0.0.8pre',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727; .NET CLR 1.1.4322; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; Browzar)',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X Mach-O; XH; rv:8.578.498) fr, Gecko/20121021 Camino/8.723+ (Firefox compatible)',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.9.2.28) Gecko/20130628 Camino/3.245.226 (MultiLang) (like Firefox/3.621.218)',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10.8; it; rv:1.93.26.2658) Gecko/20141026 Camino/2.176.223 (MultiLang) (like Firefox/3.64.2268)0',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.5; de; rv:1.9.2.28) Gecko/20120308 Camino/2.1.2 (MultiLang) (like Firefox/3.6.28)',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10.4; en; rv:1.9.0.19) Gecko/2010051911 Camino/2.0.3 (like Firefox/3.0.19)',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en; rv:1.8.1.24) Gecko/20100305 Camino/1.6.11 (like Firefox/2.0.0.24)',
                       'Mozilla/4.08 (Charon; Inferno)',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.8 (KHTML, like Gecko, Safari) Cheshire/1.0.UNOFFICIAL',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko, Safari) Cheshire/1.0.UNOFFICIAL',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/419 (KHTML, like Gecko, Safari/419.3) Cheshire/1.0.ALPHA',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; pl-PL; rv:1.0.1) Gecko/20021111 Chimera/0.6',
                       'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2228.0 Safari/537.36',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2227.1 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/41.0.2226.0 Safari/537.36',
                       'Mozilla/5.0 (Windows NT 10.0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/40.0.2214.93 Safari/537.36',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US) AppleWebKit/532.2 (KHTML, like Gecko) ChromePlus/4.0.222.3 Chrome/4.0.222.3 Safari/532.2',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.1; en-US; rv:1.9.2.3) Gecko/20100409 Firefox/3.6.3 CometBird/3.6.3',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.0; it; rv:1.9.2.16) Gecko/20110325 Firefox/3.6.16 CometBird/3.6.16',
                       'Mozilla/5.0 (Windows NT 6.2) AppleWebKit/535.7 (KHTML, like Gecko) Comodo_Dragon/16.1.1.0 Chrome/16.0.912.63 Safari/535.7',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/534.30 (KHTML, like Gecko) Comodo_Dragon/12.1.0.0 Chrome/12.0.742.91 Safari/534.30',
                       'Mozilla/5.0 (X11; U; Linux x86_64; en-US) AppleWebKit/532.5 (KHTML, like Gecko) Comodo_Dragon/4.1.1.11 Chrome/4.1.249.1042 Safari/532.5',
                       'Mozilla/5.0 (X11; Linux x86_64; rv:10.0.11) Gecko/20100101 conkeror/1.0pre (Debian-1.0~~pre+git120527-1)',
                       'Mozilla/5.0 (Windows NT 6.1; rv:16.0) Gecko/20121010 conkeror/1.0pre',
                       'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.16) Gecko/20101209 Conkeror/0.9.2 (Debian-0.9.2+git100804-1)',
                       'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.0; SV1; Crazy Browser 9.0.04)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; Crazy Browser 3.0.5) ; .NET CLR 3.0.04506.30; InfoPath.2; InfoPath.3; .NET CLR 1.1.4322; .NET4.0C; .NET4.0E; .NET CLR 2.0.50727)',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 6.2; Trident/6.0; Crazy Browser 3.1.0)',
                       'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; Crazy Browser 2.0.0)',
                       'Cyberdog/2.0 (Macintosh; PPC)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.1; WOW64; Trident/4.0; Deepnet Explorer 1.5.3; Smart 2x2; SLCC2; .NET CLR 2.0.50727; .NET CLR 3.5.30729; .NET CLR 3.0.30729; Media Center PC 6.0; .NET4.0C; .NET4.0E)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 5.1; Trident/4.0; Deepnet Explorer 1.5.2; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; InfoPath.2)',
                       'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.135 Safari/537.36 Edge/12.246',
                       'ELinks/0.9.3 (textmode; Linux 2.6.9-kanotix-8 i686; 127x41)',
                       'ELinks (0.4.3; NetBSD 3.0.2_PATCH sparc64; 80x25)',
                       'Mozilla/5.0 (X11; U; Linux x86_64; it-it) AppleWebKit/534.26+ (KHTML, like Gecko) Ubuntu/11.04 Epiphany/2.30.6',
                       'Mozilla/5.0 (X11; U; Linux x86_64; ca-ad) AppleWebKit/531.2+ (KHTML, like Gecko) Safari/531.2+ Epiphany/2.30.6',
                       'Mozilla/5.0 (X11; U; OpenBSD arm; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Safari/531.2+ Epiphany/2.30.0',
                       'Mozilla/5.0 (X11; U; Linux x86_64; en; rv:1.8.1.13) Gecko/20080322 Epiphany/2.22 Firefox/2.0.0.4',
                       'Mozilla/5.0 (Windows; U; Windows NT 6.1; x64; fr; rv:1.9.2.13) Gecko/20101203 Firebird/3.6.13',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:1.6b) Gecko/20031212 Firebird/0.7+',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; rv:40.0) Gecko/20100101 Firefox/40.1',
                       'Mozilla/5.0 (Windows NT 6.3; rv:36.0) Gecko/20100101 Firefox/36.0',
                       'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10; rv:33.0) Gecko/20100101 Firefox/33.0',
                       'Mozilla/5.0 (X11; Linux i586; rv:31.0) Gecko/20100101 Firefox/31.0',
                       'Mozilla/5.0(Windows; U; Windows NT 7.0; rv:1.9.2) Gecko/20100101 Firefox/3.6',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; en-US; rv:2.0) Treco/20110515 Fireweb Navigator/2.4',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_6; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.3.4628 Chrome/7.0.517.450 Safari/534.7',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_5; en-US) AppleWebKit/534.7 (KHTML, like Gecko) Flock/3.5.0.4568 Chrome/7.0.517.440 Safari/534.7',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_6_1; nl-nl) AppleWebKit/532.3+ (KHTML, like Gecko) Fluid/0.9.6 Safari/532.3+',
                       'Mozilla/5.0 (Macintosh; U; Intel Mac OS X 10_5_6; en-us) AppleWebKit/528.16 (KHTML, like Gecko) Fluid/0.9.6 Safari/528.16',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.9.0.8) Gecko Galeon/2.0.6 (Ubuntu 2.0.6-2)',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.8) Gecko/20050718 Galeon/1.3.20 (Debian package 1.3.20-1)',
                       'Mozilla/5.0 (X11; U; Linux i686; en-US; rv:1.7.3) Gecko/20041007 Galeon/1.3.18 (Debian package 1.3.18-1.1)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; WOW64; Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1) ; SLCC1; .NET CLR 2.0.50727; .NET CLR 3.0.04506; Media Center PC 5.0; .NET CLR 3.5.21022; GreenBrowser)',
                       'Mozilla/4.0 (compatible; MSIE 7.0; Windows NT 6.0; Trident/4.0; SLCC1; .NET CLR 2.0.50727; Media Center PC 5.0; .NET CLR 3.5.30729; .NET CLR 3.0.30729; GreenBrowser)',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X; en) AppleWebKit/418.9 (KHTML, like Gecko) Hana/1.1',
                       'Mozilla/5.0 (compatible; IBrowse 3.0; AmigaOS4.0)',
                       'Mozilla/5.0 (Macintosh; PPC Mac OS X 10_5_8) AppleWebKit/537.3+ (KHTML, like Gecko) iCab/5.0 Safari/533.16',
                       'Mozilla/5.0 (Macintosh; U; PPC Mac OS X 10_8_1; nn-no) AppleWebKit/533.21.1 (KHTML, like Gecko) iCab/4.8b Safari/533.16',
                       'iCab/4.0 (Macintosh; U; Intel Mac OS X)',
                       'Mozilla/5.0 (X11; U; Linux x86_64; en-US; rv:1.9.1.13) Gecko/20100916 Iceape/2.0.8',
                       'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121201 icecat/17.0.1',
                       'Mozilla/5.0 (X11; Linux x86_64; rv:17.0) Gecko/20121202 Firefox/17.0 Iceweasel/17.0.1',
                       'Mozilla/5.0 (X11; Linux x86_64; rv:15.0) Gecko/20120724 Debian Iceweasel/15.0',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64; Trident/7.0; AS; rv:11.0) like Gecko',
                       'Mozilla/5.0 (compatible; MSIE 10.6; Windows NT 6.1; Trident/5.0; InfoPath.2; SLCC1; .NET CLR 3.0.4506.2152; .NET CLR 3.5.30729; .NET CLR 2.0.50727) 3gpp-gba UNTRUSTED/1.0',
                       'Mozilla/5.0 (compatible; MSIE 10.0; Windows NT 7.0; InfoPath.3; .NET CLR 3.1.40767; Trident/6.0; en-IN)',
                       'Mozilla/5.0 (Windows; U; MSIE 9.0; WIndows NT 9.0; en-US))',
                       'Mozilla/5.0 (compatible; MSIE 8.0; Windows NT 6.1; Trident/4.0; GTB7.4; InfoPath.2; SV1; .NET CLR 3.3.69573; WOW64; en-US)',
                       'Mozilla/4.0(compatible; MSIE 7.0b; Windows NT 6.0)',
                       'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.4 (KHTML, like Gecko) Chrome/22.0.1250.0 Iron/22.0.2150.0 Safari/537.4',
                       'Mozilla/5.0 (Windows; U; Windows NT 5.1; pl-PL; rv:1.8.1.24pre) Gecko/20100228 K-Meleon/1.5.4',
                       ]

    i = 1
    j = 1
    _len = len(wordList)

    #x init from 0
    for x in range(140,_len):

        word = wordList[x]

        # delays for 5 seconds
        # time.sleep(5)

        # content process

        # get random user agent string in list
        # userAgentString = random.choice(User_agent_List)

        userAgentString = 'Mozilla/5.0 (X11; Ubuntu; Linux i686; rv:42.0) Gecko/20100101 Firefox/42.0'

        the_page = getResponseFromPostMethod('E', word, userAgentString)

        soup = BeautifulSoup(the_page.read())

        # find all tr tag, get text with '|' separator
        try:
            tabletag = soup.find('table', {'id': 'multiRow'})
            if(tabletag != None):
                print(tabletag)
                for trtag in tabletag.find_all('tr'):
                    f.write(trtag.get_text('|') + '\n')
                f.write(u'\n---End word---')
                print("Da get xong tu thu %d"%i)
                i = i + 1
        except AttributeError as error:
            f.write(word.decode('utf-8') + '\n')
            print error

        print("Bien chay hien tai la: %d"%j)
        print("x hien tai la %d"%x)
        j = j+1


def getResponseFromPostMethod(searchMode, word, userAgentString):

    # destination page exploit
    url = 'http://www.yellowbridge.com/chinese/dictionary.php'

    # user_agent get from http://www.useragentstring.com/
    user_agent = userAgentString

    # value is param send in post method
    # values = {'searchMode' : 'E',
    #           'word' : 'hello'
    #          }
    values = {'searchMode': searchMode,
              'word': word
              }

    # header of request
    headers = {'User-Agent': user_agent, 'Cookie':'PHPSESSID=i91k1o06482i0gt2jveko0pov1'}
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

    # initialize wordList variable
    wordList = []

    # read vocabulary from file word_list_english.txt
    word_list_file = open('word_list_english.txt', 'r')
    for line in word_list_file:
        wordList.append(line.rstrip())

    # close file word_list_english.txt
    word_list_file.close()

    filename = 'yellowbridgeOutput2.txt'

    #check filename is existed
    if os.path.isfile(filename):
        f = io.open(filename, 'a', encoding='utf-8')
    else:
        f = io.open(filename, 'w', encoding='utf-8')

    # collect chinese - english word
    main(wordList)

    # close collective file
    f.close()
