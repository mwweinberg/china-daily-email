from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv

#this will hold the output
holder = {}
#this will hold the unmatched URLs output
unmatched_holder = []



#opens the input doc
txt = open("china-daily-email-stable.csv")
#is the contents of the doc
#inputs = txt.read()

#opens the output doc
output_txt = open("china-daily-email-working.txt", "w")

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

        else:
            print "not a story from a known source"
            unmatched_holder.append(row_contents)


headliner(txt)

#this is just for debugging
#print holder
#print "unmatched holder is %s" % (unmatched_holder)

#iterates through the unmatched urls in unmatched_holder and writes them to the doc
for item in unmatched_holder:
    output_txt.write("cannot process %s" %(str(item)))
    output_txt.write("\r")
    output_txt.write("\r")

#iterates through the headlines in holder and writes them to the doc
#this is the TOC
for head, body in holder.items():
    output_txt.write(str(head))
    output_txt.write("\r")
    output_txt.write("\r")

#iterates through the headlines and body in holder and writes them to doc
#this is the body of the email

for head, body in holder.items():
    output_txt.write("\r")
    output_txt.write(str(head))
    output_txt.write("\r")
    output_txt.write("\r")
    output_txt.write(str(body))
    output_txt.write("\r")



txt.close()
output_txt.close()
