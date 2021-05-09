from GoogleNews import GoogleNews

# gn = GoogleNews
gn = GoogleNews(period='7d')
gn.search("USA")
result = gn.result()

for i in result:
    print('*'*50)
    print("Title: ", i['title'])
    print("Date: ", i['date'])
    print('Description: ', i['desc'])
    print("Link: ", i['link'])