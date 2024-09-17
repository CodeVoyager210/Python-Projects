import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

website = requests.get(url=URL).text
soup = BeautifulSoup(website, 'html.parser')
movies = [x.getText() for x in soup.find_all(name='h3', class_='title')]
movies_reversed = reversed(movies)
for _ in movies_reversed:
    with open('movies.txt', mode='a', encoding="utf-8") as mov:
        mov.write(f'{_}\n')
