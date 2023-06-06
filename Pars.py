import requests
from bs4 import BeautifulSoup

def pars_url():
    response = requests.get('https://coinmarketcap.com/')
    soup = BeautifulSoup(response.content, "html.parser")
    data = soup.find('a', {'href': '/currencies/bitcoin/markets/'}).text
    return data

if __name__ == '__main__':
    print("Bitcoin rate: ", pars_url())
