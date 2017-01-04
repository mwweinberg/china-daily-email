pages = [['http1', 'title1', 'body1'], ['http2', 'title2', 'body2'], ['http3', 'title3', 'body3']]

#access a specific item in a list nested in a list
print pages[0][0]

#add things to the list
    #create the list holder
extra = []
    #append the elements
extra.append('http4')
extra.append('title4')
extra.append('body4')
    #append the internal 'extra' list to the larger 'pages' list
pages.append(extra)
    #print the newly constructed 'pages' list
print pages

#iterate through list

    #this will print the entire sub list one entry at a time
    #topLevel will be, e.g. ['http1', 'title1', 'body1']
for topLevel in pages:
    print
    print topLevel
    print

    #this will print the sub elements
    #secondLevel will be, e.g. 'http1'
for topLevel in pages:
    for secondLevel in topLevel:
        print
        print secondLevel
        print

    #this will print the second entry in each top level
    #so it will print all of the titles
for topLevel in pages:
    print
    print topLevel[1]
    print
