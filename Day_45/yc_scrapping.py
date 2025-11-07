from bs4 import BeautifulSoup
import requests

response = requests.get("https://appbrewery.github.io/news.ycombinator.com/")
yc_web_page = response.text
# print(yc_web_page)

soup = BeautifulSoup(yc_web_page, 'html.parser')

# Selecting all the headlines 
headlines = soup.select(".storylink")
scores = soup.select(".score")
index = 0
highest_upvote = 0
highest_upvote_link = ''
highest_upvote_text = ''

for data in headlines:
    upvote = int(scores[index].text.split(' ')[0])
    print("article_text ---> ", data.text)
    print("article_link ---> ", data.get('href'))
    print("article_score ---> ", upvote)
    index += 1
    if upvote > highest_upvote :
        highest_upvote_text = data.text
        highest_upvote_link = data.get('href')
        highest_upvote = upvote

print("Highest Upvote", highest_upvote,  highest_upvote_text, highest_upvote_link)