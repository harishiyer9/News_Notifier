import xml.etree.ElementTree as ET
import urllib

#URL of top stories of The Times of India
URL = "http://timesofindia.indiatimes.com/rssfeedstopstories.cms"

#A list which holds news item in form of dictionary.
# newlist = [{title:body},{{title:body}}, ........     ]
newslist = []


'''
	Parses the top news from the TOI RSS news feed and stores it in a list named newslist
	Returns the list "newslist"
'''
def NewsList():
	fhand = urllib.urlopen(URL)
	for line in fhand:
		input = line.strip()

	news = ET.fromstring(input)
	lst = news.findall('channel/item')
	print(lst)
	for news in lst:
		newsdict = {}
		newsdict[news.find("title").text] = news.find("description").text
		newslist.append(newsdict)

	return newslist





