import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
movies_response = response.text

soup = BeautifulSoup(movies_response, 'html.parser')
movies_tags = soup.select(".article-title-description__text .title")
all_titles = [movie.text for movie in movies_tags] # list comprehension

reversed_list = all_titles[::-1] # reversed list

with open('movies.txt', mode="a") as file:
    for movie in reversed_list:
        file.write(f"{movie}\n")