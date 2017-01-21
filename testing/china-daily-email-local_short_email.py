
from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv



#data structure is now a list of dictionaries:
# holder = [{'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody},{'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody}, {'url': TheURL, 'story_title': TheTitle, 'story_body': TheBody},]


#this will hold the output of headliner() for category H stories
holder_cat_H = []
#this will hold the output of headliner() for category T stories
holder_cat_T = []
#this will hold the output of headliner() for category X stories
holder_cat_X = []
#this will hold the output of headliner() for category M stories
holder_cat_M = []
#this will hold the unmatched URLs output of headliner() - basically it catches the errors
unmatched_holder = []

#DELETE THESE ONCE YOU HAVE NEW HEADLINER BITS
holder_cat_1 = []
holder_cat_2 = []


#opens the input doc with the URLs
txt = open("tester2col.csv")
#opens the output doc where the error output data will live
output_txt = open("china-daily-email-error-output.txt", "w")

#****************************************
#*****This is for the email version******
#****************************************

#opens the target file
email_output = open("email_output.html", 'w')

#opens the content files
first_half_html = open("template_first_half.html")
second_half_html = open("template_second_half.html")

#assigns a variable name to the actual contents of those files
first_half_html_contents = first_half_html.read()
second_half_html_contents = second_half_html.read()

#****************************************
#*****End setup for the email version****
#****************************************

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

    #create a UID for each story to make email linking easier
    #it has to go outside the for loop becasue if it was inside the for loop
    #it would reset every time and all UIDs would be 1
    UID = 1
    for url, code in url_dict.items():


        if "atimes.com" in url and code == "H":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Asia Times: '
            headline = soup.find_all("h1", {"class" : "headline"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "content"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '<p>' + ''.join(element.findAll(text = True)).encode('utf-8').strip() + '</p>'

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['author'] = author_text
            temp_dict['date'] = date_text
            temp_dict['story_body'] = article_text
            temp_dict['uid'] = UID
            #now that the temp_dict is full, append it to holder
            holder_cat_H.append(temp_dict)





        elif "apnews" in url and code == "T":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Associated Press: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "cons-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "mobile"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "articleBody"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '<p>' + ''.join(element.findAll(text = True)).encode('utf-8').strip() + '</p>'

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['author'] = author_text
            temp_dict['date'] = date_text
            temp_dict['story_body'] = article_text
            temp_dict['uid'] = UID
            #now that the temp_dict is full, append it to holder
            holder_cat_T.append(temp_dict)



        elif "cpianalysis" in url and code == "X":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Policy Institute: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("p", {"class" : "footer-credits__author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "post-content clear"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '<p>' + ''.join(element.findAll(text = True)).encode('utf-8').strip() + '</p>'

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['author'] = author_text
            temp_dict['date'] = date_text
            temp_dict['story_body'] = article_text
            temp_dict['uid'] = UID
            #now that the temp_dict is full, append it to holder
            holder_cat_X.append(temp_dict)



        elif "cbc.ca" in url and code == "X":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The CBC: '
            headline = soup.find_all("h1", {"class" : "segment-headline"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("h3", {"class" : "segment-airdate"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("address", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "segment-content clearfix"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '<p>' + ''.join(element.findAll(text = True)).encode('utf-8').strip() + '</p>'

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['author'] = author_text
            temp_dict['date'] = date_text
            temp_dict['story_body'] = article_text
            temp_dict['uid'] = UID
            #now that the temp_dict is full, append it to holder
            holder_cat_X.append(temp_dict)






        elif "channelnewsasia" in url and code == "M":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChannelNewsAsia: '
            headline = soup.find_all("h1", {"class" : "news_title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "post-info-list"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("address", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "news_detail"}).findAll('p')
            #for each paragraph
            for element in article:
                #add a line break and then the text part of the paragraph
                #the .encode part fixes unicode bullshit
                article_text += '<p>' + ''.join(element.findAll(text = True)).encode('utf-8').strip() + '</p>'

            #This takes the elements and writes them to the dict
            #temp_dict will hold the info from this entry
            temp_dict = {}
            #this will load the variables into the temp_dict
            temp_dict['url'] = url
            temp_dict['story_title'] = headline_text
            temp_dict['author'] = author_text
            temp_dict['date'] = date_text
            temp_dict['story_body'] = article_text
            temp_dict['uid'] = UID
            #now that the temp_dict is full, append it to holder
            holder_cat_M.append(temp_dict)

        #if the input URL isn't in the list above, this message will be returned
        else:
            print "not a story from a known source"
            unmatched_holder.append(url)

        #increase the UID by one
        UID += 1

#run headliner()
headliner(txt)

#***************************************************
#**********This is the html output section**********
#***************************************************

#1 paste in the first half of the template
email_output.write(first_half_html_contents)

#2 write the TOC
    #Section header for Category H
    #writes the first part of the html, fills in the headline text, wraps it up
email_output.write('<h1 class="h1">'+"General Human Rights Issues"+'</h1>')
email_output.write("<br>")
for item in holder_cat_H:
    #first part of h2, plus the tag target, plus the headline, wrap it up
    email_output.write('<h3 class="h3"><a href="#'+str(item['uid'])+'">'+item['story_title']+'</a></h3>')
    email_output.write("<br>")

    #add some space
email_output.write("<br>")
email_output.write("<br>")
email_output.write("<br>")

    #section header again for Category T
email_output.write('<h1 class="h1">'+"Tibetan Issues"+'</h1>')
email_output.write("<br>")
for item in holder_cat_T:
    #first part of h2, plus the tag target, plus the headline, wrap it up
    email_output.write('<h3 class="h3"><a href="#'+str(item['uid'])+'">'+item['story_title']+'</a></h3>')
    email_output.write("<br>")

    #add some space
email_output.write("<br>")
email_output.write("<br>")
email_output.write("<br>")

    #section header again for Category X
email_output.write('<h1 class="h1">'+"Xinjiang Issues"+'</h1>')
email_output.write("<br>")
for item in holder_cat_X:
    #first part of h2, plus the tag target, plus the headline, wrap it up
    email_output.write('<h3 class="h3"><a href="#'+str(item['uid'])+'">'+item['story_title']+'</a></h3>')
    email_output.write("<br>")

    #add some space
email_output.write("<br>")
email_output.write("<br>")
email_output.write("<br>")

    #section header again for Category M
email_output.write('<h1 class="h1">'+"Other Ethnic Minority Issues"+'</h1>')
email_output.write("<br>")
for item in holder_cat_M:
    #first part of h2, plus the tag target, plus the headline, wrap it up
    email_output.write('<h3 class="h3"><a href="#'+str(item['uid'])+'">'+item['story_title']+'</a></h3>')
    email_output.write("<br>")



#3 create a border between the TOC and the body
email_output.write("<br>")
email_output.write("<br>")
email_output.write("************************")
email_output.write("<br>")
email_output.write("<br>")

#4a iterates though the stories in category H
email_output.write('<h1 class="h1">'+'General Human Rights Issues'+'</h1>')
email_output.write("<br>")
for item in holder_cat_H:
    email_output.write("<br>")
    #this is the headline with an anchor tag
    email_output.write('<h3 class="h3" id="'+str(item['uid'])+'">'+item['story_title']+'</h3>')
    email_output.write("<br />")
    #this is the URL that links out
    email_output.write('<a href="'+item['url']+'">'+item['url']+'</a>')
    email_output.write("<br />")
    #this is the author
    email_output.write(item['author'])
    email_output.write("<br />")
    #this is the date
    email_output.write(item['date'])
    email_output.write("<br />")
    email_output.write("<br />")
    #this is the body
    email_output.write(item['story_body'])
    email_output.write("<br />")
    email_output.write('<a href="#top">Back to top</a>')
    email_output.write("<br />")
    email_output.write("<br />")

#4b iterates though the stories in category T
email_output.write('<h1 class="h1">'+'Tibetan Issues'+'</h1>')
email_output.write("<br>")
for item in holder_cat_T:
    email_output.write("<br>")
    #this is the headline with an anchor tag
    email_output.write('<h3 class="h3" id="'+str(item['uid'])+'">'+item['story_title']+'</h3>')
    email_output.write("<br />")
    #this is the URL that links out
    email_output.write('<a href="'+item['url']+'">'+item['url']+'</a>')
    email_output.write("<br />")
    #this is the author
    email_output.write(item['author'])
    email_output.write("<br />")
    #this is the date
    email_output.write(item['date'])
    email_output.write("<br />")
    email_output.write("<br />")
    #this is the body
    email_output.write(item['story_body'])
    email_output.write("<br />")
    email_output.write('<a href="#top">Back to top</a>')
    email_output.write("<br />")
    email_output.write("<br />")

#4c iterates though the stories in category X
email_output.write('<h1 class="h1">'+'Xinjiang Issues'+'</h1>')
email_output.write("<br>")
for item in holder_cat_X:
    email_output.write("<br>")
    #this is the headline with an anchor tag
    email_output.write('<h3 class="h3" id="'+str(item['uid'])+'">'+item['story_title']+'</h3>')
    email_output.write("<br />")
    #this is the URL that links out
    email_output.write('<a href="'+item['url']+'">'+item['url']+'</a>')
    email_output.write("<br />")
    #this is the author
    email_output.write(item['author'])
    email_output.write("<br />")
    #this is the date
    email_output.write(item['date'])
    email_output.write("<br />")
    email_output.write("<br />")
    #this is the body
    email_output.write(item['story_body'])
    email_output.write("<br />")
    email_output.write('<a href="#top">Back to top</a>')
    email_output.write("<br />")
    email_output.write("<br />")

#4d iterates though the stories in category M
email_output.write('<h1 class="h1">'+'Other Ethnic Minority Issues'+'</h1>')
email_output.write("<br>")
for item in holder_cat_M:
    email_output.write("<br>")
    #this is the headline with an anchor tag
    email_output.write('<h3 class="h3" id="'+str(item['uid'])+'">'+item['story_title']+'</h3>')
    email_output.write("<br />")
    #this is the URL that links out
    email_output.write('<a href="'+item['url']+'">'+item['url']+'</a>')
    email_output.write("<br />")
    #this is the author
    email_output.write(item['author'])
    email_output.write("<br />")
    #this is the date
    email_output.write(item['date'])
    email_output.write("<br />")
    email_output.write("<br />")
    #this is the body
    email_output.write(item['story_body'])
    email_output.write("<br />")
    email_output.write('<a href="#top">Back to top</a>')
    email_output.write("<br />")
    email_output.write("<br />")





#x paste the end html
email_output.write(second_half_html_contents)


#***************************************************
#**********End html output section******************
#***************************************************

#***************************************************
#**********This is the text output section**********
#***************************************************

#1iterates through the unmatched urls in unmatched_holder and writes them to the doc

for item in unmatched_holder:
    output_txt.write("cannot process %s" %(str(item)))
    output_txt.write("\n")
    output_txt.write("\r")
    output_txt.write("\r")


#keeping this text output section in case it is useful
#if not entire section can be deleted
#it will still produce the error document
"""

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
"""

#***************************************************
#**********End text output section******************
#***************************************************

email_output.close()
first_half_html.close()
second_half_html.close()

txt.close()

output_txt.close()
