import requests
from bs4 import BeautifulSoup
import datetime



def get_gist_content(repo_url):
    html = requests.get(repo_url).text
    soup = BeautifulSoup(html, 'html.parser')
    button = soup.find_all('div', class_='file-actions flex-order-2 pt-0')
    raw_url = f"https://gist.github.com/{button[0].contents[1].attrs['href'][1:]}"
    
    raw_content = requests.get(raw_url).json()
    return raw_content


def countdown(timestamp:int):
    now = datetime.datetime.now().replace(microsecond=0)
    end = datetime.datetime.fromtimestamp(timestamp).replace(microsecond=0)

    return (end-now)