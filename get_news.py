import requests


def get_news():
    url = "https://www.nytimes.com/search?query=covid"
    response = requests.get(url)
    print(response.text)
