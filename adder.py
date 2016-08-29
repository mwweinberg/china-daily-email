from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv


#initiates the dictionary to hold the output

holder = {}


#opens the input doc
txt = open("adder.txt")
#is the contents of the doc

#opens the output doc
output_txt = open("adder_output.txt", "w")

print txt

def headliner(url):

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
            print "didn't find a matching URL"

headliner(txt)
#this is just for debugging
print holder




txt.close()
output_txt.close()
