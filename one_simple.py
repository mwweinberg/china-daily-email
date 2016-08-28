from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv


#initiates the dictionary to hold the output

holder = []


#opens the input doc
txt = open("one-url.txt")
#is the contents of the doc
txt_contents = txt.read()

#opens the output doc
output_txt = open("output.txt", "w")

print txt_contents

def headliner(url):

    if "rfa" in url:
        #opens the url for read access
        this_url = urllib.urlopen(url).read()
        #creates a new BS holder based on the URL
        soup = BeautifulSoup(this_url, 'lxml')
        #creates the sections
        headline = soup.find_all('title')
        print "headline = %s" % (headline)

        body = soup.find("p", {"id" : "storytext"})
        print "bodytext = %s" % (body)

        output_txt.write(str(headline))
        output_txt.write("\n")
        output_txt.write(str(headline))
        output_txt.write("\n")
        output_txt.write(str(body))
    else:
        print "not an RFA story"

headliner(txt_contents)
txt.close()
output_txt.close()
