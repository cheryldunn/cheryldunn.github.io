#get the stuff we need for web scraping
import nltk
from bs4 import BeautifulSoup
from urllib import request

#store the url we are scraping
url = "https://github.com/humanitiesprogramming/scraping-corpus"

#go to the request library, find the url we identified to scrape, and try to read it
#using that url, get the html from it
html = request.urlopen(url).read()

#I took the url and turned it into a soup object

soup = BeautifulSoup(html, 'lxml')
our_text = soup.text
#look for all the anchor tabs between 0 and 10 and store them in links
links = soup.find_all('a')[0:10]

#print(links)

#print(our_text[0:2000])
#replace the line breaks with spaces (\n is a line break)
#print(soup.text.replace('\n', ' '))

#
links_html = soup.select('td.content a')
this_link = links_html[0]

#print(this_link['href'])
urls=[]
#take each link and make a new list w/processed urls
for link in links_html:
    to_append = link['href'].replace('blob/', '')
    urls.append("https://raw.githubusercontent.com" + to_append)

#test_url = urls[3]
corpus_texts = []
for url in urls:
    html = request.urlopen(url).read()
    soup = BeautifulSoup(html,"lxml")
    text = soup.text.replace('\n', '')
    corpus_texts.append(text)
    print("Scraping" + url)

print(len(corpus_texts))
print(len(corpus_texts[0]))

this_text = corpus_texts[0]
process_this_text = nltk.word_tokenize(this_text)
print(process_this_text[0:20])
#gives most common 50 words in this book
print(nltk.FreqDist(process_this_text).most_common(50))
