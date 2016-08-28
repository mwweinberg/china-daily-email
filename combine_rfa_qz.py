from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv



#opens the input doc
txt = open("qz-rfa.csv")
#is the contents of the doc
#inputs = txt.read()

#opens the output doc
output_txt = open("output.txt", "w")

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
            headline_text = ''
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()
            print headline_text



            #creats the body text
            #This turns the htlm text into regular text
            article_text = ''
            #This finds each paragraph
            article = soup.find("div", {"id" : "storytext"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()
            print article_text
            #body = soup.find("div", {"id" : "storytext"})




            output_txt.write(str(headline_text))
            output_txt.write("\n")
            output_txt.write("\r")
            output_txt.write("\r")
            output_txt.write(str(headline_text))
            output_txt.write("\n")
            output_txt.write(str(article_text))
            output_txt.write("\n")
            output_txt.write("\r")
            output_txt.write("\r")
            output_txt.write("\r")
            output_txt.write("\r")

        if "qz" in row_contents:
            #opens the url for read access
            this_url = urllib.urlopen(row_contents).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')


            #creates the headline section
            headline_text = ''
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()
            print headline_text



            #creats the body text
            #This turns the htlm text into regular text
            article_text = ''
            #This finds each paragraph
            article = soup.find("div", {"class" : "item-body"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()
            print article_text





            output_txt.write(str(headline_text))
            output_txt.write("\n")
            output_txt.write("\r")
            output_txt.write("\r")
            output_txt.write(str(headline_text))
            output_txt.write("\n")
            output_txt.write(str(article_text))
            output_txt.write("\n")
            output_txt.write("\r")
            output_txt.write("\r")
            output_txt.write("\r")
            output_txt.write("\r")

        else:
            print "not an RFA story"

headliner(txt)


txt.close()
output_txt.close()
