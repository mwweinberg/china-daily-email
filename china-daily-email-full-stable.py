import email
import getpass, imaplib
import os
import sys
from bs4 import BeautifulSoup
import urllib
#csv is for the csv writer
import csv
import smtplib
import imapclient




#download attachment

detach_dir = '.'
if 'attachments' not in os.listdir(detach_dir):
    os.mkdir('attachments')

user = open("user.txt", 'r')
password = open("password.txt", 'r')

userName = user.read()
passwd = password.read()

try:
    imapSession = imaplib.IMAP4_SSL('imap.gmail.com')
    typ, accountDetails = imapSession.login(userName, passwd)
    if typ != 'OK':
        print 'Not able to sign in!'
        raise

    imapSession.select('INBOX')
    typ, data = imapSession.search(None, 'ALL')
    if typ != 'OK':
        print 'Error searching Inbox.'
        raise

    # Iterating over all emails
    for msgId in data[0].split():
        typ, messageParts = imapSession.fetch(msgId, '(RFC822)')
        if typ != 'OK':
            print 'Error fetching mail.'
            raise

        emailBody = messageParts[0][1]
        mail = email.message_from_string(emailBody)
        for part in mail.walk():
            if part.get_content_maintype() == 'multipart':
                # print part.as_string()
                continue
            if part.get('Content-Disposition') is None:
                # print part.as_string()
                continue
            fileName = part.get_filename()

            if bool(fileName):
                filePath = os.path.join(detach_dir, 'attachments', fileName)
                if not os.path.isfile(filePath) :
                    print fileName
                    fp = open(filePath, 'wb')
                    fp.write(part.get_payload(decode=True))
                    fp.close()
    imapSession.close()
    imapSession.logout()




    #generate the email text

    #this will hold the output
    holder = {}
    #this will hold the unmatched URLs output
    unmatched_holder = []



    #opens the input doc
    txt = open("./attachments/china-daily-email-stable.csv")
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



            elif "qz" in row_contents:
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

            elif "latimes" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'LA Times: '
                headline = soup.find_all('h1')
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph

                article = soup.find("div", {"class" : "trb_ar_page"}).findAll('p')
                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "wsj" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'WSJ: '
                headline = soup.find_all('h1')
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph

                article = soup.find("div", {"id" : "wsj-article-wrap"}).findAll('p')
                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "chinadigitaltimes" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'China Digital Times: '
                headline = soup.find_all('h1')
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph

                article = soup.find("div", {"class" : "entry"}).findAll('p')
                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "tchrd" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'TCHRD: '
                headline = soup.find_all('h1')
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph

                article = soup.find("div", {"class" : "entry"}).findAll('p')
                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "scmp" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'SCMP: '
                headline = soup.find_all('h1', {"itemprop": "name headline"}, {"class": "title", "id":"page-title"})
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph
                article = soup.find_all('p')

                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "caixin" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'Caixin: '
                headline = soup.find_all('h1')
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                #this line adds the URL to the output text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph

                article = soup.find("div", {"id" : "txt_content", 'style' : 'font-size:14px;'}).findAll('p')
                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "reuters" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'Reuters: '
                headline = soup.find_all('h1')
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                #this line adds the URL to the output text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph

                article = soup.find("span", {"id" : "article-text"}).findAll('p')
                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "xinhuanet" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'Xinhua: '
                headline = soup.find_all('span', {'id':'bltitle'})
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                #this line adds the URL to the output text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph

                article = soup.find("span", {"id" : "content", "class":"hei14 pcCon"}).findAll('p')
                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "theguardian" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'The Guardian: '
                headline = soup.find_all('h1', {"class":"content__headline js-score", "itemprop":"headline"})
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()




                #creats the body text
                #This turns the html text into regular text
                #this line adds the URL to the output text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph

                article = soup.find("div", {"class" : "content__article-body from-content-api js-article__body", "itemprop":"articleBody", "data-test-id":"article-review-body"}).findAll('p')
                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            elif "scmp" in row_contents:
                #opens the url for read access
                this_url = urllib.urlopen(row_contents).read()
                #creates a new BS holder based on the URL
                soup = BeautifulSoup(this_url, 'lxml')

                #creates the headline section
                headline_text = 'SCMP: '
                headline = soup.find_all('h1', {"itemprop": "name headline"}, {"class": "title", "id":"page-title"})
                for element in headline:
                        headline_text += ''.join(element.findAll(text = True)).encode('utf-8').strip()
                        headline_text += "\n"




                #creats the body text
                #This turns the html text into regular text
                article_text = row_contents + "\n" + "\r"
                #This finds each paragraph
                article = soup.find_all('p')

                #for each paragraph
                for element in article:
                    #add a line break and then the text part of the paragraph
                    #the .encode part fixes unicode bullshit
                    article_text += '\n' + ''.join(element.findAll(text = True)).encode('utf-8').strip()

                holder[headline_text] = article_text

            else:
                print "not a story from a known source"
                unmatched_holder.append(row_contents)


    headliner(txt)


    #iterates through the unmatched urls in unmatched_holder and writes them to the doc
    for item in unmatched_holder:
        output_txt.write("cannot process %s" %(str(item)))
        output_txt.write("\n")
        output_txt.write("\r")
        output_txt.write("\r")

    #iterates through the headlines in holder and writes them to the doc
    #this is the TOC
    for head, body in holder.items():
        output_txt.write(str(head))
        output_txt.write("\r")

    #creates space between list of headlines and the stories
    output_txt.write("\n")
    output_txt.write("\n")
    output_txt.write("\n")
    output_txt.write("*************************************")
    output_txt.write("\n")

    #iterates through the headlines and body in holder and writes them to doc
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



    txt.close()
    output_txt.close()


    # send the email

    #imports U/P from other files that are not shared on github
    user = open("user.txt", 'r')
    password = open("password.txt", 'r')
    attachment = open("china-daily-email-working.txt", 'r')
    user_contents = user.read()
    password_contents = password.read()
    attachment_contents = attachment.read()

    #formats the body of the email corectly

    body = 'Subject: Exciting Robot Delivery\n' + attachment_contents

    #print body





    #SENDING SECTION

    #creates smtp object, which is a connection to the server using TLS
    smtpObj = smtplib.SMTP('smtp.gmail.com', 587)
    #opens connection to server
    smtpObj.ehlo()
    #starts encryption
    smtpObj.starttls()
    #login to server
    smtpObj.login(user_contents, password_contents)
    #send email
    smtpObj.sendmail(user_contents, 'hello@michaelweinberg.org', body)
    #disconnects from the server
    smtpObj.quit()





    user.close()
    password.close()
    attachment.close()

    #delete the local email body text and the local version of the attachment

    os.remove("china-daily-email-working.txt")
    os.remove("./attachments/china-daily-email-stable.csv")

    #delete the email on the server

    #logs in
    imapObj = imapclient.IMAPClient('imap.gmail.com', ssl = True)
    imapObj.login(user_contents, password_contents)

    #picks a folder
    imapObj.select_folder('INBOX', readonly=False)

    #identifies the messages
    UIDs = imapObj.search(['ALL'])

    #sets them to delete
    imapObj.delete_messages(UIDs)
    #and actually deletes them
    imapObj.expunge()

    #logs out
    imapObj.logout()

    #imports U/P from other files that are not shared on github
    user = open("user.txt", 'r')
    password = open("password.txt", 'r')

    user_contents = user.read()
    password_contents = password.read()


    #deletes everything in the Inbox

    box = imaplib.IMAP4_SSL('imap.gmail.com')
    box.login(user_contents,password_contents)
    box.select('Inbox')
    typ, data = box.search(None, 'ALL')
    for num in data[0].split():
       box.store(num, '+FLAGS', '\\Deleted')
    box.expunge()
    box.close()
    box.logout()


#this closes out the try: that starts in the attachmetn download section
except :
    print 'Not able to download all attachments.'
