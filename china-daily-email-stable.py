from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv

#this will hold the output
holder = {}



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



        if "qz" in row_contents:
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

        else:
            print "not a story from a known source"

headliner(txt)

#this is just for debugging
print holder

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
