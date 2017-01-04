
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



#this will hold the output of headliner()
holder = {}
holder2 = []
#this will hold the unmatched URLs output of headliner() - basically it catches the errors
unmatched_holder = []



#opens the input doc with the URLs
txt = open("tester.csv")
#is the contents of the doc
#inputs = txt.read()

#opens the output doc where the output data will live
output_txt = open("china-daily-email-local-output.txt", "w")
output_txt2 = open("china-daily-email-local-output2.txt", "w")


def headliner(url):

    #iterate through the urls

    parsed_urls = csv.reader(url)
    for row in parsed_urls:

        number = 0
        story_URL = row[number]
        print "story_URL = %s" %(story_URL)
        number += 1

        #TODO:changes you need to make to each entry
        #stop adding the URL to the start of the body text
            #delete "article_text = story_URL + "\n" + "\r""
        #declare article_text now that you have delted that line
            #change "article_text += '\n' + ''.join . . ."
            #to "article_text = '\n' + ''.join . . ."
            #(change += to just =)
        #add the holder2 section at the end


        if "rfa" in story_URL:
            #opens the url for read access
            this_url = urllib.urlopen(story_URL).read()
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

            holder[headline_text] = article_text

            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['story_URL'] = story_URL
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
            holder2.append(temp_dict)



        elif "qz" in story_URL:
            #opens the url for read access
            this_url = urllib.urlopen(story_URL).read()
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



            holder[headline_text] = article_text

            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['story_URL'] = story_URL
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
            holder2.append(temp_dict)



        elif "sixthtone" in story_URL:
            #opens the url for read access
            this_url = urllib.urlopen(story_URL).read()
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

            holder[headline_text] = article_text

            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['story_URL'] = story_URL
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
            holder2.append(temp_dict)

        elif "cpianalysis" in story_URL:
            #opens the url for read access
            this_url = urllib.urlopen(story_URL).read()
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

            holder[headline_text] = article_text

            #this is the new section for the new holder2
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['story_URL'] = story_URL
            temp_dict['story_title'] = headline_text
            temp_dict['story_body'] = article_text

            #now that the temp_dict is full, append it to holder2
            holder2.append(temp_dict)


        #if the input URL isn't in the list above, this message will be returned
        else:
            print "not a story from a known source"
            unmatched_holder.append(story_URL)

#run headliner()
headliner(txt)

#these are just prints for troubleshooting


print
#for each dictionary in the list holder2
for topLevel in holder2:
    #print the entry the corresponds with the story_title key
    print topLevel['story_title']
print

#1iterates through the unmatched urls in unmatched_holder and writes them to the doc
for item in unmatched_holder:
    output_txt.write("cannot process %s" %(str(item)))
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write("\r")

#1**********holder2 version**************
for item in unmatched_holder:
    output_txt2.write("cannot process %s" %(str(item)))
    output_txt2.write("\n")
    output_txt2.write("\r")
    output_txt2.write("\r")


#2iterates through the headlines in holder and writes them to the doc
#this is the TOC
#this is where "headline_text" becomes "head" and "article_text" becomes "body"
for head, body in holder.items():
    output_txt.write(str(head))
    output_txt.write("\r")

#2**********holder2 version**************
for topLevel in holder2:
    output_txt2.write(topLevel['story_title'])
    output_txt2.write("\r")

#3creates space between list of headlines and the stories
output_txt.write("\n")
output_txt.write("\n")
output_txt.write("\n")
output_txt.write("*************************************")
output_txt.write("\n")

#3**********holder2 version**************
output_txt.write("\n")
output_txt.write("\n")
output_txt.write("\n")
output_txt.write("*************************************")
output_txt.write("\n")

#4iterates through the headlines and body in holder and writes them to doc
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

#4**********holder2 version**************
for topLevel in holder2:
    output_txt2.write("\r")
    output_txt2.write("\n")
    output_txt2.write(topLevel['story_title'])
    output_txt2.write("\n")
    output_txt2.write("\r")
    output_txt2.write(topLevel['story_URL'])
    output_txt2.write("\n")
    output_txt2.write("\r")
    output_txt2.write(topLevel['story_body'])
    output_txt2.write("\n")
    output_txt2.write("\r")
    output_txt2.write("\n")
    output_txt2.write("\n")
    output_txt2.write("\n")



txt.close()
output_txt.close()
output_txt2.close()
