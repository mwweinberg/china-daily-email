pages = [{'url': 'http1', 'title':'title1', 'body':'body1'}, {'url': 'http2', 'title':'title2', 'body':'body2'}, {'url': 'http3', 'title':'title3', 'body':'body3'}]

#access a specific item nested in a dictionary
print pages[0]['url']

#add things to the list

    #create the new dictionary
extra = {}

    #load in the elements
extra['url'] = 'http4'
extra['title'] = 'title4'
extra['body'] = 'body4'

    #add the new dictionary to pages
pages.append(extra)

    #print the new pages
print pages


#iterate through the list

    #this prints each dictionary one at a time
for topLevel in pages:
    print
    print topLevel
    print

    #this will print each element in the dictionary one at a time
for topLevel in pages:
    #the first term describes the key, the second one describes the entry
    for key, entry in topLevel.items():
        print
        print key
        print entry
        print
    #you don't need to print both
    for key, entry in topLevel.items():
        print
        print entry
        print

    #this will print all of the titles
        #for each dictionary...
for topLevel in pages:
    # prints each entry with the 'title' key for each dictionary
    print topLevel['title']
