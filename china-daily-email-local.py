
import time
import email
import getpass, imaplib
import os
import sys
from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv
import smtplib
import imapclient

"""
Included Sources:

1843 Magazine
BBC
Caixin
ChannelNewsAsia
ChinaChange
China Digital Times
ChinaFile
China Media Project
China Policy Institute
Chublic Opinion
Dui Hua Human Rights Journal
East Asia Forum
Foreign Policy
Free Tibet
The Guardian
LA Times
Quartz
Radio Free Asia
Reuters
SCMP
Sixth Tone
Sydney Morning Herald
TCHRD
Tibetan Review
Wall Street Journal
Washington Post
Xinhua
Xinjiang Review


Tried and Failed to Add:

nytimes
nybooks
hong kong free press
the nanfang
world policy journal
phayul
the national interest
ICT
yahoo
politics from the provinces
Medium
the diplomat

"""



#this will hold the output
holder = {}
#this will hold the unmatched URLs output
unmatched_holder = []



#opens the input doc
txt = open("./attachments/tester.csv")
#is the contents of the doc
#inputs = txt.read()

#opens the output doc
output_txt = open("china-daily-email-local-output.txt", "w")

print txt

def headliner(url):

    #iterate through the urls

    parsed_urls = csv.reader(url)
    for row in parsed_urls:

        number = 0
        row_contents = row[number]
        print row_contents
        number += 1


        if "rfa" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Radio Free Asia: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph
            article = soup.find("div", {"id" : "storytext"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text



        elif "qz" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')


            #creates the headline section
            headline_text = 'Quartz: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the htlm text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph
            article = soup.find("div", {"class" : "item-body"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()



            holder[headline_text] = article_text



        elif "foreignpolicy" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Policy: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "shares-position"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "sixthtone" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Sixth Tone: '
            headline = soup.find_all('h3', {"class":"heading-1"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "content"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "washingtonpost" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Washington Post: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"id" : "article-body"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "latimes" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'LA Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "trb_ar_page"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "wsj" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'WSJ: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"id" : "wsj-article-wrap"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "chinadigitaltimes" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Digital Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "entry"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "tchrd" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'TCHRD: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "entry"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "caixin" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Caixin: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"id" : "txt_content", 'style' : 'font-size:14px;'}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "reuters" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Reuters: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("span", {"id" : "article-text"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "xinhuanet" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Xinhua: '
            headline = soup.find_all('span', {'id':'bltitle'})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("span", {"id" : "content", "class":"hei14 pcCon"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "theguardian" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Guardian: '
            headline = soup.find_all('h1', {"class":"content__headline js-score", "itemprop":"headline"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "content__article-body from-content-api js-article__body", "itemprop":"articleBody", "data-test-id":"article-review-body"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "scmp" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'SCMP: '
            headline = soup.find_all('h1', {"itemprop": "name headline"}, {"class": "title", "id":"page-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()
                    headline_text += "\n"




            #creats the body text
            #This turns the html text into regular text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph
            article = soup.find_all('p')

            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "eastasiaforum" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'East Asia Forum: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("section", {"class" : "content"}).find_all('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "smh" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Sydney Morning Herald: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "article__body"}).find_all('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "cpianalysis" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Poilcy Institute: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "post-content clear"}).find_all('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text

        elif "xinjiangreview" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Xinjiang Review: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            article_text = row_contents + "\n" + "\r"
            #This finds each paragraph

            article = soup.find("div", {"class" : "entry"}).find_all('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            holder[headline_text] = article_text


        elif "chinafile" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'ChinaFile: '
		    headline = soup.find_all('h1')
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "panel-pane pane-node-content"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text



        elif "chinachange" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'ChinaChange: '
		    headline = soup.find_all('h1')
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "entry-content clearfix"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text


        elif "channelnewsasia" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'ChannelNewsAsia: '
		    headline = soup.find_all("h1")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "news_detail"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text


        elif "tibetanreview" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'Tibetan Review: '
		    headline = soup.find_all("h1")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "entry"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text

        elif "duihuahrjournal" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'Dui Hua Human Rights Journal: '
		    headline = soup.find_all("h3")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "post-body entry-content"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text

        elif "cmp.hku" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'China Media Project: '
		    headline = soup.find_all("h2")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "entry"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text


        elif "bbc" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'BBC: '
		    headline = soup.find_all("h2")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "story-body__inner"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text



        elif "1843magazine" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = '1843 Magazine: '
		    headline = soup.find_all("h1")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("section", {"class" : "article__body page-and-article-content"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text


        elif "chublicopinion" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'Chublic Opinion: '
		    headline = soup.find_all("h1")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "entry-content"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text


        elif "freetibet" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'Free Tibet: '
		    headline = soup.find_all("h1")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("section", {"id" : "content"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text



        elif "globaltimes" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'Global Times: '
		    headline = soup.find_all("h3")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "span12 row-content"}).find_all('p')
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text


        elif "supremepeoplescourtmonitor" in row_contents:
		    #opens the url for read access
		    this_url = urllib.urlopen(row_contents).read()
		    #creates a new BS holder based on the URL
		    soup = BeautifulSoup(this_url, 'lxml')

		    #creates the headline section
		    headline_text = 'SPC Monitor: '
		    headline = soup.find_all("h1")
		    for element in headline:
		            headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


		    #creats the body text
		    #This turns the html text into regular text
		    #this line adds the URL to the output text
		    article_text = row_contents + "\n" + "\r"
		    #This finds each paragraph

		    article = soup.find("div", {"class" : "entry-content"}).find_all("p")
		    #for each paragraph
		    for element in article:
		        #add a line break and then the text part of the paragraph
		        #the .encode part fixes unicode bullshit
		        article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

		    holder[headline_text] = article_text











        else:
            print "not a story from a known source"
            unmatched_holder.append(row_contents)


headliner(txt)


#iterates through the unmatched urls in unmatched_holder and writes them to the doc
for item in unmatched_holder:
    output_txt.write("cannot process %s" %(str(item)))
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write("\r")

#iterates through the headlines in holder and writes them to the doc
#this is the TOC
for head, body in holder.items():
    output_txt.write(str(head))
    output_txt.write("\r")

#creates space between list of headlines and the stories
output_txt.write("\n")
output_txt.write("\n")
output_txt.write("\n")
output_txt.write("*************************************")
output_txt.write("\n")

#iterates through the headlines and body in holder and writes them to doc
#this is the body of the email

for head, body in holder.items():
    output_txt.write("\r")
    output_txt.write("\n")
    output_txt.write(str(head))
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write(str(body))
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write("\n")
    output_txt.write("\n")
    output_txt.write("\n")



txt.close()
output_txt.close()
