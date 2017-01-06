
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
#add the holder2 section at the end
# remove the old holder section
    # delete "holder[headline_text] = article_text"


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

#data structure is now a list of dictionaries:
# holder = [{'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody},{'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody}, {'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody},]

# legacy holder for initial testing
#holder = []
#this will hold the output of headliner() for category 1 stories
holder_cat_1 = []
#this will hold the output of headliner() for category 2 stories
holder_cat_2 = []
#this will hold the unmatched URLs output of headliner() - basically it catches the errors
unmatched_holder = []



#opens the input doc with the URLs
txt = open("tester2col.csv")
#is the contents of the doc
#inputs = txt.read()

#opens the output doc where the output data will live
output_txt = open("china-daily-email-local-output2-new.txt", "w")

#this builds a set of dictionaries with all of the stories and their contents
#sorted by the category code
def headliner(url):

    #creates dictionary called url_dict out of csv file
    url_csv = csv.reader(txt)
    url_dict = dict((rows[0],rows[1]) for rows in url_csv)


    # assigns meaningful variable name to the columns in the csv
    # and iterates through them one at a time
    # looking for a condition match
    for url, code in url_dict.items():

        # if the story is from RFA and the code is 1
        if "rfa" in url and code == '1':
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Radio Free Asia: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            #This turns the html text into regular text
            #This finds each paragraph
            article = soup.find("div", {"id" : "storytext"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()



            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder1
            #because it is story category 1
            holder_cat_1.append(temp_dict)

        # if the story is from RFA and the code is 2
        elif "rfa" in url and code == '2':
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Radio Free Asia: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            #This turns the html text into regular text
            #This finds each paragraph
            article = soup.find("div", {"id" : "storytext"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()



            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
            #because it is story category 2
            holder_cat_2.append(temp_dict)


        elif "qz" in url and code == "1":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')


            #creates the headline section
            headline_text = 'Quartz: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the htlm text into regular text
            #This finds each paragraph
            article = soup.find("div", {"class" : "item-body"}).findAll('p')
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

        elif "qz" in url and code == "2":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')


            #creates the headline section
            headline_text = 'Quartz: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the htlm text into regular text
            #This finds each paragraph
            article = soup.find("div", {"class" : "item-body"}).findAll('p')
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
            holder_cat_2.append(temp_dict)


        elif "sixthtone" in url and code == "1":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Sixth Tone: '
            headline = soup.find_all('h3', {"class":"heading-1"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #This finds each paragraph

            article = soup.find("div", {"class" : "content"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()



            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
            holder_cat_1.append(temp_dict)

        elif "sixthtone" in url and code == "2":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Sixth Tone: '
            headline = soup.find_all('h3', {"class":"heading-1"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #This finds each paragraph

            article = soup.find("div", {"class" : "content"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()



            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
            holder_cat_2.append(temp_dict)

        elif "cpianalysis" in url and code == "1":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Policy Institute: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            #This finds each paragraph

            article = soup.find("div", {"class" : "post-content clear"}).find_all('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
            holder_cat_1.append(temp_dict)

        elif "cpianalysis" in url and code == "2":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Policy Institute: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




            #creats the body text
            #This turns the html text into regular text
            #this line adds the URL to the output text
            #This finds each paragraph

            article = soup.find("div", {"class" : "post-content clear"}).find_all('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text = '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
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
