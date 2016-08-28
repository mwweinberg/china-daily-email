from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv


#initiates the dictionary to hold the output

holder = []


#opens the doc
txt = open("one-url.txt")
#is the contents of the doc
txt_contents = txt.read()

print txt_contents

def headliner(url):

    if "www.rfa.org" in url:
        #opens the url for read access
        this_url = urllib.urlopen(url).read()
        #creates a new BS holder based on the URL
        soup = BeautifulSoup(this_url, 'lxml')
        #creates the sections
        headline = soup.find_all('title')
        print "headline = %s" % (headline)

        body = soup.find("div", {"id" : "storytext"})
        print "bodytext = %s" % (body)
    else:
        print "not an RFA story"

headliner(txt_contents)
