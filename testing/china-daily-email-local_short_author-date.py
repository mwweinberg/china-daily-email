
from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv

#TODO in holder():changes you need to make to each entry
#stop adding the URL to the start of the body text
    #delete "article_text = url + "\n" + "\r""
#declare article_text now that you have delted that line
    #change "article_text += '\n' + ''.join . . ."
    #to "article_text = '\n' + ''.join . . ."
    #(change += to just =)
#add the holder_cat_2 section at the end
# remove the old holder section
    # delete "holder[headline_text] = article_text"




#data structure is now a list of dictionaries:
# holder = [{'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody},{'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody}, {'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody},]


#this will hold the output of headliner() for category 1 stories
holder_cat_1 = []
#this will hold the output of headliner() for category 2 stories
holder_cat_2 = []
#this will hold the unmatched URLs output of headliner() - basically it catches the errors
unmatched_holder = []


#opens the input doc with the URLs
txt = open("tester2colauth.csv")
#opens the output doc where the output data will live
output_txt = open("china-daily-email-local-output.txt", "w")

#this builds a set of dictionaries with all of the stories and their contents
#sorted by the category code
#once these exist they can be used to write the output file below
def headliner(url):

    #creates dictionary called url_dict out of csv file
    url_csv = csv.reader(txt)
    url_dict = dict((rows[0],rows[1]) for rows in url_csv)


    # assigns meaningful variable name to the columns in the csv
    # and iterates through them one at a time
    # looking for a condition match for both URL element and category
    # there is a code block for each URL x the number of categories
    for url, code in url_dict.items():


        if "jeromecohen" in url and code == '1':
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Jerry\"s Blog: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            #This finds each paragraph
            article = soup.find("div", {"class" : "body entry-content"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text
            #now that the temp_dict is full, append it to holder_cat_1
            #because it is story category 1
            holder_cat_1.append(temp_dict)


        elif "jeromecohen" in url and code == '2':
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Jerry\"s Blog: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            #This finds each paragraph
            article = soup.find("div", {"class" : "body entry-content"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text
            #now that the temp_dict is full, append it to holder_cat_2
            #because it is story category 2
            holder_cat_2.append(temp_dict)


        elif "caixin" in url and code == "1":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Caixin: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            #This turns the htlm text into regular text
            #This finds each paragraph
            article = soup.find("div", {"class" : "cons-box"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #this is the new section for the new holder
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text
            #now that the temp_dict is full, append it to holder
            holder_cat_1.append(temp_dict)

        elif "caixin" in url and code == "2":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Caixin: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            #This finds each paragraph
            article = soup.find("div", {"class" : "cons-box"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text
            #now that the temp_dict is full, append it to holder
            holder_cat_2.append(temp_dict)


        elif "telegraph" in url and code == "1":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Telegraph: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            #This finds each paragraph
            article = soup.find("article", {"itemprop" : "articleBody"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text
            #now that the temp_dict is full, append it to holder_cat_2
            holder_cat_1.append(temp_dict)

        elif "telegraph" in url and code == "2":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Telegraph: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()


            #creats the body text
            #This finds each paragraph
            article = soup.find("article", {"itemprop" : "articleBody"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text
            #now that the temp_dict is full, append it to holder_cat_2
            holder_cat_2.append(temp_dict)

        

        #if the input URL isn't in the list above, this message will be returned
        else:
            print "not a story from a known source"
            unmatched_holder.append(url)

#run headliner()
headliner(txt)



#1iterates through the unmatched urls in unmatched_holder and writes them to the doc

for item in unmatched_holder:
    output_txt.write("cannot process %s" %(str(item)))
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write("\r")


#2iterates through the headlines in holder and writes them to the doc
#this is the TOC
output_txt.write("Category 1 headlines")
output_txt.write("\n")
output_txt.write("\r")
for topLevel in holder_cat_1:
    output_txt.write(topLevel['story_title'])
    output_txt.write("\r")

output_txt.write("\n")
output_txt.write("\r")

output_txt.write("Category 2 headlines")
output_txt.write("\n")
output_txt.write("\r")
for topLevel in holder_cat_2:
    output_txt.write(topLevel['story_title'])
    output_txt.write("\r")

#3creates space between list of headlines and the stories

output_txt.write("\n")
output_txt.write("\n")
output_txt.write("\n")
output_txt.write("*************************************")
output_txt.write("\n")


#4a iterates through the stories in category 1
output_txt.write("#############Category 1 Stories###########")
for topLevel in holder_cat_1:
    output_txt.write("\r")
    output_txt.write("\n")
    output_txt.write(topLevel['story_title'])
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write(topLevel['url'])
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write(topLevel['story_body'])
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write("\n")
    output_txt.write("\n")
    output_txt.write("\n")

#4a iterates through the stories in category 2
output_txt.write("#############Category 2 Stories###########")
for topLevel in holder_cat_2:
    output_txt.write("\r")
    output_txt.write("\n")
    output_txt.write(topLevel['story_title'])
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write(topLevel['url'])
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write(topLevel['story_body'])
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write("\n")
    output_txt.write("\n")
    output_txt.write("\n")

txt.close()

output_txt.close()
