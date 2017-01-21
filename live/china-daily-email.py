
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
txt = open("input.csv")
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



        #1. work as-is



        if "atimes.com" in url and code == "h":
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

        elif "atimes.com" in url and code == "t":
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
            holder_cat_T.append(temp_dict)

        elif "atimes.com" in url and code == "x":
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
            holder_cat_X.append(temp_dict)

        elif "atimes.com" in url and code == "m":
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
            holder_cat_M.append(temp_dict)




        elif "apnews" in url and code == "h":
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
            holder_cat_H.append(temp_dict)

        elif "apnews" in url and code == "t":
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

        elif "apnews" in url and code == "x":
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
            holder_cat_X.append(temp_dict)

        elif "apnews" in url and code == "m":
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
            holder_cat_M.append(temp_dict)




        elif "cbc.ca" in url and code == "h":
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
            holder_cat_H.append(temp_dict)

        elif "cbc.ca" in url and code == "t":
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
            holder_cat_T.append(temp_dict)

        elif "cbc.ca" in url and code == "x":
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

        elif "cbc.ca" in url and code == "m":
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
            holder_cat_M.append(temp_dict)




        elif "channelnewsasia" in url and code == "h":
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
            holder_cat_H.append(temp_dict)

        elif "channelnewsasia" in url and code == "t":
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
            holder_cat_T.append(temp_dict)

        elif "channelnewsasia" in url and code == "x":
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
            holder_cat_X.append(temp_dict)

        elif "channelnewsasia" in url and code == "m":
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




        elif "cpianalysis" in url and code == "h":
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
            holder_cat_H.append(temp_dict)

        elif "cpianalysis" in url and code == "t":
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
            holder_cat_T.append(temp_dict)

        elif "cpianalysis" in url and code == "x":
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

        elif "cpianalysis" in url and code == "m":
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
            holder_cat_M.append(temp_dict)





        elif "chinachange" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChinaChange: '
            headline = soup.find_all("span", {"class" : "current"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "nothing"})
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
            article = soup.find("div", {"class" : "entry-content clearfix"}).findAll('p')
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

        elif "chinachange" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChinaChange: '
            headline = soup.find_all("span", {"class" : "current"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "nothing"})
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
            article = soup.find("div", {"class" : "entry-content clearfix"}).findAll('p')
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

        elif "chinachange" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChinaChange: '
            headline = soup.find_all("span", {"class" : "current"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "nothing"})
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
            article = soup.find("div", {"class" : "entry-content clearfix"}).findAll('p')
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

        elif "chinachange" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChinaChange: '
            headline = soup.find_all("span", {"class" : "current"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "nothing"})
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
            article = soup.find("div", {"class" : "entry-content clearfix"}).findAll('p')
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





        elif "chinadaily" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The China Daily: '
            headline = soup.find_all("div", {"class" : "lft_art"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "info_l"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "Content"}).findAll('p')
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

        elif "chinadaily" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The China Daily: '
            headline = soup.find_all("div", {"class" : "lft_art"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "info_l"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "Content"}).findAll('p')
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

        elif "chinadaily" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The China Daily: '
            headline = soup.find_all("div", {"class" : "lft_art"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "info_l"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "Content"}).findAll('p')
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

        elif "chinadaily" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The China Daily: '
            headline = soup.find_all("div", {"class" : "lft_art"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("ul", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "info_l"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "Content"}).findAll('p')
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





        elif "chublicopinion" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Chublic Opinion: '
            headline = soup.find_all("span", {"class" : "breadcrumbs-current"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "entry-date published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "chublicopinion" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Chublic Opinion: '
            headline = soup.find_all("span", {"class" : "breadcrumbs-current"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "entry-date published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "chublicopinion" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Chublic Opinion: '
            headline = soup.find_all("span", {"class" : "breadcrumbs-current"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "entry-date published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "chublicopinion" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Chublic Opinion: '
            headline = soup.find_all("span", {"class" : "breadcrumbs-current"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "entry-date published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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





        elif "theguardian" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Guardian: '
            headline = soup.find_all('h1', {"class":"content__headline js-score", "itemprop":"headline"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "content__article-body from-content-api js-article__body", "itemprop":"articleBody", "data-test-id":"article-review-body"}).findAll('p')
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

        elif "theguardian" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Guardian: '
            headline = soup.find_all('h1', {"class":"content__headline js-score", "itemprop":"headline"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "content__article-body from-content-api js-article__body", "itemprop":"articleBody", "data-test-id":"article-review-body"}).findAll('p')
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

        elif "theguardian" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Guardian: '
            headline = soup.find_all('h1', {"class":"content__headline js-score", "itemprop":"headline"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "content__article-body from-content-api js-article__body", "itemprop":"articleBody", "data-test-id":"article-review-body"}).findAll('p')
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

        elif "theguardian" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Guardian: '
            headline = soup.find_all('h1', {"class":"content__headline js-score", "itemprop":"headline"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "content__article-body from-content-api js-article__body", "itemprop":"articleBody", "data-test-id":"article-review-body"}).findAll('p')
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





        elif "reuters" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Reuters: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "timestamp"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("span", {"id" : "article-text"}).findAll('p')
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

        elif "reuters" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Reuters: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "timestamp"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("span", {"id" : "article-text"}).findAll('p')
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

        elif "reuters" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Reuters: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "timestamp"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("span", {"id" : "article-text"}).findAll('p')
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

        elif "reuters" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Reuters: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "timestamp"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("span", {"id" : "article-text"}).findAll('p')
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





        elif "smh.com" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Sydney Morning Herald: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("h5", {"rel" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article__body"}).findAll('p')
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

        elif "smh.com" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Sydney Morning Herald: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("h5", {"rel" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article__body"}).findAll('p')
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

        elif "smh.com" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Sydney Morning Herald: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("h5", {"rel" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article__body"}).findAll('p')
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

        elif "smh.com" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Sydney Morning Herald: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("h5", {"rel" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article__body"}).findAll('p')
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





        elif "tibetanreview" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Tibetan Review: '
            headline = soup.find_all('h1')
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
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "tibetanreview" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Tibetan Review: '
            headline = soup.find_all('h1')
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
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "tibetanreview" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Tibetan Review: '
            headline = soup.find_all('h1')
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
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "tibetanreview" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Tibetan Review: '
            headline = soup.find_all('h1')
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
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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




        elif "yahoo.com" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Yahoo News: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "date Fz(11px) D(ib) Mb(4px)"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"class" : "author-link Td(u):h Fz(12px) Lh(18px) C(#000) Fw(b) Mend(3px) Td(n)"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "canvas-body C(#26282a) Wow(bw) Cl(start) Mb(20px) Ff($ff-secondary) Fz(15px) Lh(1.6)"}).findAll('p')
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

        elif "yahoo.com" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Yahoo News: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "date Fz(11px) D(ib) Mb(4px)"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"class" : "author-link Td(u):h Fz(12px) Lh(18px) C(#000) Fw(b) Mend(3px) Td(n)"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "canvas-body C(#26282a) Wow(bw) Cl(start) Mb(20px) Ff($ff-secondary) Fz(15px) Lh(1.6)"}).findAll('p')
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

        elif "yahoo.com" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Yahoo News: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "date Fz(11px) D(ib) Mb(4px)"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"class" : "author-link Td(u):h Fz(12px) Lh(18px) C(#000) Fw(b) Mend(3px) Td(n)"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "canvas-body C(#26282a) Wow(bw) Cl(start) Mb(20px) Ff($ff-secondary) Fz(15px) Lh(1.6)"}).findAll('p')
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

        elif "yahoo.com" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Yahoo News: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "date Fz(11px) D(ib) Mb(4px)"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"class" : "author-link Td(u):h Fz(12px) Lh(18px) C(#000) Fw(b) Mend(3px) Td(n)"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "canvas-body C(#26282a) Wow(bw) Cl(start) Mb(20px) Ff($ff-secondary) Fz(15px) Lh(1.6)"}).findAll('p')
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




        #2. work well enough but may need mods later



        elif "cmp.hku" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Media Project: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "published-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "cmp.hku" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Media Project: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "published-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "cmp.hku" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Media Project: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "published-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "cmp.hku" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Media Project: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "published-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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





        elif "chinafile" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChinaFile: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("li", {"class" : "create-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("li", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "panel-pane pane-node-content"}).findAll('p')
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

        elif "chinafile" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChinaFile: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("li", {"class" : "create-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("li", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "panel-pane pane-node-content"}).findAll('p')
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

        elif "chinafile" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChinaFile: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("li", {"class" : "create-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("li", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "panel-pane pane-node-content"}).findAll('p')
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

        elif "chinafile" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'ChinaFile: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("li", {"class" : "create-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("li", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "panel-pane pane-node-content"}).findAll('p')
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




        elif "politicsfromthe" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Chinese Politics from the Provinces: '
            headline = soup.find_all("h3", {"class" : "post-title entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #no author
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "post-body entry-content"})
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

        elif "politicsfromthe" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Chinese Politics from the Provinces: '
            headline = soup.find_all("h3", {"class" : "post-title entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #no author
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "post-body entry-content"})
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

        elif "politicsfromthe" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Chinese Politics from the Provinces: '
            headline = soup.find_all("h3", {"class" : "post-title entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #no author
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "post-body entry-content"})
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

        elif "politicsfromthe" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Chinese Politics from the Provinces: '
            headline = soup.find_all("h3", {"class" : "post-title entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #no author
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "post-body entry-content"})
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





        elif "duihuahrjournal" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Dui Hua Human Rights Journal: '
            headline = soup.find_all('h3')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("abbr", {"class" : "published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "post-body entry-content"}).findAll('p')
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

        elif "duihuahrjournal" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Dui Hua Human Rights Journal: '
            headline = soup.find_all('h3')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("abbr", {"class" : "published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "post-body entry-content"}).findAll('p')
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

        elif "duihuahrjournal" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Dui Hua Human Rights Journal: '
            headline = soup.find_all('h3')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("abbr", {"class" : "published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "post-body entry-content"}).findAll('p')
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

        elif "duihuahrjournal" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Dui Hua Human Rights Journal: '
            headline = soup.find_all('h3')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("abbr", {"class" : "published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "post-body entry-content"}).findAll('p')
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




        elif "globaltimes" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Global Times: '
            headline = soup.find_all('h3')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #unneeded
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "span12 row-content"}).findAll('p')
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

        elif "globaltimes" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Global Times: '
            headline = soup.find_all('h3')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #unneeded
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "span12 row-content"}).findAll('p')
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

        elif "globaltimes" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Global Times: '
            headline = soup.find_all('h3')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #unneeded
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "span12 row-content"}).findAll('p')
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

        elif "globaltimes" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Global Times: '
            headline = soup.find_all('h3')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #unneeded
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "span12 row-content"}).findAll('p')
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





        elif "globeandmail" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Globe and Mail: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "dateModified"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "author creator"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article-enriched-body"}).findAll('p')
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

        elif "globeandmail" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Globe and Mail: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "dateModified"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "author creator"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article-enriched-body"}).findAll('p')
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

        elif "globeandmail" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Globe and Mail: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "dateModified"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "author creator"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article-enriched-body"}).findAll('p')
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

        elif "globeandmail" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Globe and Mail: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "dateModified"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "author creator"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article-enriched-body"}).findAll('p')
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





        elif "jeromecohen" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Jerry\'s Blog: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "body entry-content"}).findAll('p')
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

        elif "jeromecohen" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Jerry\'s Blog: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "body entry-content"}).findAll('p')
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

        elif "jeromecohen" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Jerry\'s Blog: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "body entry-content"}).findAll('p')
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

        elif "jeromecohen" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Jerry\'s Blog: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"itemprop" : "name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "body entry-content"}).findAll('p')
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




        elif "opendemocracy" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Open Democracy: '
            headline = soup.find_all("h2", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #trb_ar_dateline
            date = soup.find_all("abbr", {"class" : "published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "authors pf-author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "grid-8 alpha omega article-content"}).findAll('p')
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

        elif "opendemocracy" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Open Democracy: '
            headline = soup.find_all("h2", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #trb_ar_dateline
            date = soup.find_all("abbr", {"class" : "published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "authors pf-author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "grid-8 alpha omega article-content"}).findAll('p')
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

        elif "opendemocracy" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Open Democracy: '
            headline = soup.find_all("h2", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #trb_ar_dateline
            date = soup.find_all("abbr", {"class" : "published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "authors pf-author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "grid-8 alpha omega article-content"}).findAll('p')
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

        elif "opendemocracy" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Open Democracy: '
            headline = soup.find_all("h2", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #trb_ar_dateline
            date = soup.find_all("abbr", {"class" : "published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "authors pf-author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "grid-8 alpha omega article-content"}).findAll('p')
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






        elif "people.cn" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The People\'s Daily: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "wb_1 clear"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "wb_12 wb_12b clear"}).findAll('p')
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

        elif "people.cn" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The People\'s Daily: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "wb_1 clear"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "wb_12 wb_12b clear"}).findAll('p')
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

        elif "people.cn" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The People\'s Daily: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "wb_1 clear"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "wb_12 wb_12b clear"}).findAll('p')
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

        elif "people.cn" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The People\'s Daily: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "wb_1 clear"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "wb_12 wb_12b clear"}).findAll('p')
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





        elif "phayul" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Phayul: '
            headline = soup.find_all("span", {"id" : "_ctl1_lblHeading"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #included in body text
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #included in body text
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"style" : "padding-top:5px"})
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

        elif "phayul" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Phayul: '
            headline = soup.find_all("span", {"id" : "_ctl1_lblHeading"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #included in body text
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #included in body text
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"style" : "padding-top:5px"})
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

        elif "phayul" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Phayul: '
            headline = soup.find_all("span", {"id" : "_ctl1_lblHeading"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #included in body text
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #included in body text
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"style" : "padding-top:5px"})
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

        elif "phayul" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Phayul: '
            headline = soup.find_all("span", {"id" : "_ctl1_lblHeading"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #included in body text
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #included in body text
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"style" : "padding-top:5px"})
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




        elif "rfa.org" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Radio Free Asia: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"id" : "story_date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "cons-author-txt"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "storytext"}).findAll('p')
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

        elif "rfa.org" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Radio Free Asia: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"id" : "story_date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "cons-author-txt"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "storytext"}).findAll('p')
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

        elif "rfa.org" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Radio Free Asia: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"id" : "story_date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "cons-author-txt"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "storytext"}).findAll('p')
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

        elif "rfa.org" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Radio Free Asia: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"id" : "story_date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "cons-author-txt"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "storytext"}).findAll('p')
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




        elif "sixthtone" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Sixth Tone: '
            headline = soup.find_all('h3', {"class":"heading-1"})
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
            author = soup.find_all("div", {"class" : "wraptext-headeline"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
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

        elif "sixthtone" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Sixth Tone: '
            headline = soup.find_all('h3', {"class":"heading-1"})
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
            author = soup.find_all("div", {"class" : "wraptext-headeline"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
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
            holder_cat_T.append(temp_dict)

        elif "sixthtone" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Sixth Tone: '
            headline = soup.find_all('h3', {"class":"heading-1"})
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
            author = soup.find_all("div", {"class" : "wraptext-headeline"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
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
            holder_cat_X.append(temp_dict)

        elif "sixthtone" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Sixth Tone: '
            headline = soup.find_all('h3', {"class":"heading-1"})
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
            author = soup.find_all("div", {"class" : "wraptext-headeline"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
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
            holder_cat_M.append(temp_dict)




        elif "scmp.com" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'South China Morning Post: '
            headline = soup.find_all("div", {"class" : "node-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"itemprop" : "dateCreated"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "scmp-v2-author-name clearfix"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p")
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

        elif "scmp.com" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'South China Morning Post: '
            headline = soup.find_all("div", {"class" : "node-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"itemprop" : "dateCreated"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "scmp-v2-author-name clearfix"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p")
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

        elif "scmp.com" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'South China Morning Post: '
            headline = soup.find_all("div", {"class" : "node-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"itemprop" : "dateCreated"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "scmp-v2-author-name clearfix"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p")
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

        elif "scmp.com" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'South China Morning Post: '
            headline = soup.find_all("div", {"class" : "node-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"itemprop" : "dateCreated"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "scmp-v2-author-name clearfix"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p")
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





        elif "supchina" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'SupChina: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "time"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"rel" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article_text"}).findAll('p')
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

        elif "supchina" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
           #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'SupChina: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "time"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"rel" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article_text"}).findAll('p')
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

        elif "supchina" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
           #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'SupChina: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "time"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"rel" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article_text"}).findAll('p')
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

        elif "supchina" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'SupChina: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "time"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"rel" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "article_text"}).findAll('p')
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




        elif "supremepeoplescourtmonitor" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Supreme People\'s Court Monitor: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "entry-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"nothing" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "supremepeoplescourtmonitor" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Supreme People\'s Court Monitor: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "entry-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"nothing" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "supremepeoplescourtmonitor" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Supreme People\'s Court Monitor: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "entry-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"nothing" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "supremepeoplescourtmonitor" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Supreme People\'s Court Monitor: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "entry-date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"nothing" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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




        elif "telegraph" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Telegraph: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "article-date-published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("article", {"itemprop" : "articleBody"}).findAll('p')
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

        elif "telegraph" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Telegraph: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "article-date-published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("article", {"itemprop" : "articleBody"}).findAll('p')
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

        elif "telegraph" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Telegraph: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "article-date-published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("article", {"itemprop" : "articleBody"}).findAll('p')
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

        elif "telegraph" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Telegraph: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("time", {"class" : "article-date-published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("article", {"itemprop" : "articleBody"}).findAll('p')
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





        elif "tibet.net" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'CTA website: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "single_meta_item single_meta_date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # single_byline
            author = soup.find_all("div", {"id" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "tibet.net" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'CTA website: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "single_meta_item single_meta_date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # single_byline
            author = soup.find_all("div", {"id" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "tibet.net" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'CTA website: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "single_meta_item single_meta_date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # single_byline
            author = soup.find_all("div", {"id" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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

        elif "tibet.net" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'CTA website: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "single_meta_item single_meta_date"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # single_byline
            author = soup.find_all("div", {"id" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content"}).findAll('p')
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




        elif "whatsonweibo" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'What\'s On Weibo: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "entry-date published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # author-name
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content col-md-9 col-md-push-3"}).findAll('p')
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

        elif "whatsonweibo" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'What\'s On Weibo: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "entry-date published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # author-name
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content col-md-9 col-md-push-3"}).findAll('p')
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

        elif "whatsonweibo" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'What\'s On Weibo: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "entry-date published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # author-name
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content col-md-9 col-md-push-3"}).findAll('p')
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

        elif "whatsonweibo" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'What\'s On Weibo: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"class" : "entry-date published"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # author-name
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry-content col-md-9 col-md-push-3"}).findAll('p')
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






        elif "xinhuanet" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Xinhua: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "info"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # author-name
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "content"}).findAll('p')
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

        elif "xinhuanet" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Xinhua: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "info"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # author-name
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "content"}).findAll('p')
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

        elif "xinhuanet" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Xinhua: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "info"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # author-name
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "content"}).findAll('p')
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

        elif "xinhuanet" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Xinhua: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "info"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # author-name
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "content"}).findAll('p')
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



        #3. these have parts of the code zeroed out that will need to be fixed later




        elif "bangkokpost" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Bangkok Post: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "articleContents"}).findAll('p')
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

        elif "bangkokpost" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Bangkok Post: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "articleContents"}).findAll('p')
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

        elif "bangkokpost" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Bangkok Post: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "articleContents"}).findAll('p')
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

        elif "bangkokpost" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Bangkok Post: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("span", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "articleContents"}).findAll('p')
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





        elif "bbc.com" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The BBC: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date date--v2
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "byline__name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "story-body__inner"}).findAll('p')
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

        elif "bbc.com" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The BBC: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date date--v2
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "byline__name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "story-body__inner"}).findAll('p')
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

        elif "bbc.com" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The BBC: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date date--v2
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "byline__name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "story-body__inner"}).findAll('p')
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

        elif "bbc.com" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The BBC: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date date--v2
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "byline__name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "story-body__inner"}).findAll('p')
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




        elif "bloomberg" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Bloomberg: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date date--v2
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("address", {"class" : "lede-text-only__byline"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "body-copy"}).findAll('p')
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

        elif "bloomberg" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Bloomberg: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date date--v2
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("address", {"class" : "lede-text-only__byline"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "body-copy"}).findAll('p')
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

        elif "bloomberg" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Bloomberg: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date date--v2
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("address", {"class" : "lede-text-only__byline"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "body-copy"}).findAll('p')
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

        elif "bloomberg" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Bloomberg: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date date--v2
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("address", {"class" : "lede-text-only__byline"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "body-copy"}).findAll('p')
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





        elif "caixin" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Caixin: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "cons-author-txt"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "cons-box"}).findAll('p')
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

        elif "caixin" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Caixin: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "cons-author-txt"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "cons-box"}).findAll('p')
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

        elif "caixin" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Caixin: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "cons-author-txt"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "cons-box"}).findAll('p')
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

        elif "caixin" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Caixin: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "cons-author-txt"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "cons-box"}).findAll('p')
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




        elif "chinadigitaltimes" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Digital Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "chinadigitaltimes" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Digital Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "chinadigitaltimes" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Digital Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "chinadigitaltimes" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Digital Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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




        elif "foreignpolicy" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Policy: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("li", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "description"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "shares-position"}).findAll('p')
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

        elif "foreignpolicy" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Policy: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("li", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "description"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "shares-position"}).findAll('p')
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

        elif "foreignpolicy" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Policy: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("li", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "description"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "shares-position"}).findAll('p')
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

        elif "foreignpolicy" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Policy: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            date = soup.find_all("li", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("span", {"class" : "description"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "shares-position"}).findAll('p')
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




        elif "freetibet" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Free Tibet: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date-display-single
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("section", {"id" : "content"}).findAll('p')
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

        elif "freetibet" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Free Tibet: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date-display-single
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("section", {"id" : "content"}).findAll('p')
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

        elif "freetibet" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Free Tibet: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date-display-single
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("section", {"id" : "content"}).findAll('p')
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

        elif "freetibet" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Free Tibet: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date-display-single
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("section", {"id" : "content"}).findAll('p')
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





        elif "qz.com" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Quartz: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # "timestamp"
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # "author-name"
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "item-body"}).findAll('p')
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

        elif "qz.com" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Quartz: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # "timestamp"
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # "author-name"
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "item-body"}).findAll('p')
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

        elif "qz.com" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Quartz: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # "timestamp"
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # "author-name"
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "item-body"}).findAll('p')
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

        elif "qz.com" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Quartz: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # "timestamp"
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # "author-name"
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "item-body"}).findAll('p')
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




        elif "tchrd" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Tibetan Centre for Human Rights and Democracy: '
            headline = soup.find_all('h1')
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
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "tchrd" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Tibetan Centre for Human Rights and Democracy: '
            headline = soup.find_all('h1')
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
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "tchrd" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Tibetan Centre for Human Rights and Democracy: '
            headline = soup.find_all('h1')
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
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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

        elif "tchrd" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Tibetan Centre for Human Rights and Democracy: '
            headline = soup.find_all('h1')
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
            author = soup.find_all("span", {"class" : "byline__author-name"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"class" : "entry"}).findAll('p')
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




        elif "washingtonpost" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Washington Post: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # timestamp
            date = soup.find_all("span", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # name
            author = soup.find_all("span", {"itemprop" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "article-body"}).findAll('p')
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

        elif "washingtonpost" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Washington Post: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # timestamp
            date = soup.find_all("span", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # name
            author = soup.find_all("span", {"itemprop" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "article-body"}).findAll('p')
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

        elif "washingtonpost" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Washington Post: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # timestamp
            date = soup.find_all("span", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # name
            author = soup.find_all("span", {"itemprop" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "article-body"}).findAll('p')
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

        elif "washingtonpost" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Washington Post: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # timestamp
            date = soup.find_all("span", {"itemprop" : "datePublished"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # name
            author = soup.find_all("span", {"itemprop" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find("div", {"id" : "article-body"}).findAll('p')
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



        #4. Headline only


        elif "foreignaffairs" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Affairs: '
            headline = soup.find_all("h2", {"class" : "sticky-nav--article__title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "foreignaffairs" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Affairs: '
            headline = soup.find_all("h2", {"class" : "sticky-nav--article__title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "foreignaffairs" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Affairs: '
            headline = soup.find_all("h2", {"class" : "sticky-nav--article__title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "foreignaffairs" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Foreign Affairs: '
            headline = soup.find_all("h2", {"class" : "sticky-nav--article__title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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





        elif "france24" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'France 24: '
            headline = soup.find_all("h1", {"class" : "title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            # article = soup.find_all("div", {"class" : "bd"})
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "france24" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'France 24: '
            headline = soup.find_all("h1", {"class" : "title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            # article = soup.find_all("div", {"class" : "bd"})
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "france24" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'France 24: '
            headline = soup.find_all("h1", {"class" : "title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            # article = soup.find_all("div", {"class" : "bd"})
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "france24" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'France 24: '
            headline = soup.find_all("h1", {"class" : "title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            # article = soup.find_all("div", {"class" : "bd"})
            article = soup.find_all("div", {"class" : "nothing"})
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




        elif "latimes" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The LA Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #trb_ar_dateline
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"itemprop" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            #trb_ar_page
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "latimes" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The LA Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #trb_ar_dateline
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"itemprop" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            #trb_ar_page
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "latimes" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The LA Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #trb_ar_dateline
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"itemprop" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            #trb_ar_page
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "latimes" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The LA Times: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #trb_ar_dateline
            date = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("a", {"itemprop" : "author"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            #trb_ar_page
            article = soup.find_all("div", {"class" : "nothing"})
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





        elif "www.voa" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Voice of America: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"id" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            # article = soup.find("div", {"class" : "wysiwyg"}).findAll('p')
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "www.voa" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Voice of America: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"id" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            # article = soup.find("div", {"class" : "wysiwyg"}).findAll('p')
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "www.voa" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Voice of America: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"id" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            # article = soup.find("div", {"class" : "wysiwyg"}).findAll('p')
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "www.voa" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Voice of America: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # date
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            author = soup.find_all("div", {"id" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            # article = soup.find("div", {"class" : "wysiwyg"}).findAll('p')
            article = soup.find_all("div", {"class" : "nothing"})
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





        elif "wsj.com" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Wall Street Journal: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # timestamp
            date = soup.find_all("time", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # byline
            author = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            #  article = soup.find("div", {"class" : "wsj-snippet-body"}).findAll('p')
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "wsj.com" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Wall Street Journal: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # timestamp
            date = soup.find_all("time", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # byline
            author = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            #  article = soup.find("div", {"class" : "wsj-snippet-body"}).findAll('p')
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "wsj.com" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Wall Street Journal: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # timestamp
            date = soup.find_all("time", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # byline
            author = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            #  article = soup.find("div", {"class" : "wsj-snippet-body"}).findAll('p')
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "wsj.com" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Wall Street Journal: '
            headline = soup.find_all('title')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            # timestamp
            date = soup.find_all("time", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            # byline
            author = soup.find_all("div", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creats the body text
            article_text = ""
            #This finds each paragraph
            #  article = soup.find("div", {"class" : "wsj-snippet-body"}).findAll('p')
            article = soup.find_all("div", {"class" : "nothing"})
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


        #5. cannot be used as-is


        elif "1843magazine" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = '1843 Magazine: '
            headline = soup.find_all('h1')
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
            article = soup.find("section", {"class" : "article__body page-and-article-content"}).findAll('p')
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

        elif "1843magazine" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = '1843 Magazine: '
            headline = soup.find_all('h1')
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
            article = soup.find("section", {"class" : "article__body page-and-article-content"}).findAll('p')
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

        elif "1843magazine" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = '1843 Magazine: '
            headline = soup.find_all('h1')
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
            article = soup.find("section", {"class" : "article__body page-and-article-content"}).findAll('p')
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

        elif "1843magazine" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = '1843 Magazine: '
            headline = soup.find_all('h1')
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
            article = soup.find("section", {"class" : "article__body page-and-article-content"}).findAll('p')
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




        elif "chinafilminsider" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Film Insider: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "chinafilminsider" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Film Insider: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "chinafilminsider" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Film Insider: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "chinafilminsider" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'China Film Insider: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("span", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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



        elif "thediplomat" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Diplomat: '
            headline = soup.find_all("h1", {"itemprop" : "name"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "postBody ng-scope"})
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

        elif "thediplomat" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Diplomat: '
            headline = soup.find_all("h1", {"itemprop" : "name"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "postBody ng-scope"})
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

        elif "thediplomat" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Diplomat: '
            headline = soup.find_all("h1", {"itemprop" : "name"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "postBody ng-scope"})
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

        elif "thediplomat" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Diplomat: '
            headline = soup.find_all("h1", {"itemprop" : "name"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "postBody ng-scope"})
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




        elif "eastasiaforum" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'East Asia Forum: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("section", {"class" : "content"})
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

        elif "eastasiaforum" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'East Asia Forum: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("section", {"class" : "content"})
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

        elif "eastasiaforum" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'East Asia Forum: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("section", {"class" : "content"})
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

        elif "eastasiaforum" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'East Asia Forum: '
            headline = soup.find_all('h1')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("section", {"class" : "content"})
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




        elif "economist.com" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Economist: '
            headline = soup.find_all("span", {"class" : "flytitle-and-title__title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "blog-post__text"})
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

        elif "economist.com" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Economist: '
            headline = soup.find_all("span", {"class" : "flytitle-and-title__title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "blog-post__text"})
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

        elif "economist.com" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Economist: '
            headline = soup.find_all("span", {"class" : "flytitle-and-title__title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "blog-post__text"})
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

        elif "economist.com" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Economist: '
            headline = soup.find_all("span", {"class" : "flytitle-and-title__title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("h2", {"class" : "date-header"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "blog-post__text"})
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




        elif "hongkongfp" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Hong Kong Free Press: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #unneeded
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "hongkongfp" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Hong Kong Free Press: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #unneeded
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "hongkongfp" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Hong Kong Free Press: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #unneeded
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "hongkongfp" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'Hong Kong Free Press: '
            headline = soup.find_all("h1", {"class" : "entry-title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #unneeded
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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




        elif "savetibet" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'International Campaign for Tibet: '
            headline = soup.find_all("span", {"class" : "trail-end"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "savetibet" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'International Campaign for Tibet: '
            headline = soup.find_all("span", {"class" : "trail-end"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "savetibet" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'International Campaign for Tibet: '
            headline = soup.find_all("span", {"class" : "trail-end"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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

        elif "savetibet" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'International Campaign for Tibet: '
            headline = soup.find_all("span", {"class" : "trail-end"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "nothing"})
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




        elif "medium.com" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Medium: '
            headline = soup.find_all("p", {"class" : "graf graf--p graf--leading"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p", {"class" : "graf graf--p graf-after--p"})
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

        elif "medium.com" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Medium: '
            headline = soup.find_all("p", {"class" : "graf graf--p graf--leading"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p", {"class" : "graf graf--p graf-after--p"})
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

        elif "medium.com" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Medium: '
            headline = soup.find_all("p", {"class" : "graf graf--p graf--leading"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p", {"class" : "graf graf--p graf-after--p"})
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

        elif "medium.com" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The Medium: '
            headline = soup.find_all("p", {"class" : "graf graf--p graf--leading"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p", {"class" : "graf graf--p graf-after--p"})
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



        elif "nationalinterest" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The National Interest: '
            headline = soup.find_all("h1", {"class" : "page-title title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "node-content"})
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

        elif "nationalinterest" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The National Interest: '
            headline = soup.find_all("h1", {"class" : "page-title title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "node-content"})
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

        elif "nationalinterest" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The National Interest: '
            headline = soup.find_all("h1", {"class" : "page-title title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "node-content"})
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

        elif "nationalinterest" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The National Interest: '
            headline = soup.find_all("h1", {"class" : "page-title title"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("div", {"class" : "node-content"})
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



        elif "nybooks" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The New York Review of Books: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("section", {"class" : "article_body"})
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

        elif "nybooks" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The New York Review of Books: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("section", {"class" : "article_body"})
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

        elif "nybooks" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The New York Review of Books: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("section", {"class" : "article_body"})
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

        elif "nybooks" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The New York Review of Books: '
            headline = soup.find_all('h2')
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("section", {"class" : "article_body"})
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




        elif "nytimes" in url and code == "h":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The New York Times: '
            headline = soup.find_all("h6", {"class" : "kicker"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p", {"class" : "story-body-text story-content"})
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

        elif "nytimes" in url and code == "t":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The New York Times: '
            headline = soup.find_all("h6", {"class" : "kicker"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p", {"class" : "story-body-text story-content"})
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

        elif "nytimes" in url and code == "x":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The New York Times: '
            headline = soup.find_all("h6", {"class" : "kicker"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p", {"class" : "story-body-text story-content"})
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

        elif "nytimes" in url and code == "m":
            #opens the url for read access
            this_url = urllib.urlopen(url).read()
            #creates a new BS holder based on the URL
            soup = BeautifulSoup(this_url, 'lxml')

            #creates the headline section
            headline_text = 'The New York Times: '
            headline = soup.find_all("h6", {"class" : "kicker"})
            for element in headline:
                    headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the date section
            #initializes the variable
            date_text = ""
            #finds the relevant section
            #didn't look for this
            date = soup.find_all("div", {"class" : "span8 text-left"})
            #isolates the content of the variable and strips out the html
            for element in date:
                    date_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the author section
            #initializes the variable
            author_text = ""
            #finds the relevant section
            #didn't look for this
            author = soup.find_all("a", {"class" : "nothing"})
            #isolates the content of the variable and strips out the html
            for element in author:
                    author_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()

            #creates the body text
            article_text = ""
            #This finds each paragraph
            article = soup.find_all("p", {"class" : "story-body-text story-content"})
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

#2 write the top anchor so "back to top" links work
email_output.write('<h1 class="h1" id = "top"></h1>')

#3 write the TOC
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



#4 create a border between the TOC and the body
email_output.write("<br>")
email_output.write("<br>")
email_output.write("************************")
email_output.write("<br>")
email_output.write("<br>")

#5a iterates though the stories in category H
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

#5b iterates though the stories in category T
email_output.write("<br>")
email_output.write("------")
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

#5c iterates though the stories in category X
email_output.write("<br>")
email_output.write("------")
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

#5d iterates though the stories in category M
email_output.write("<br>")
email_output.write("------")
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





#6 paste the end html
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
