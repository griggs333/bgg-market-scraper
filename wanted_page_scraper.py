import requests as req
from bs4 import BeautifulSoup as bs
from dataclasses import dataclass


game_page_prefix = "https://boardgamegeek.com"


@dataclass
class Game:
    name: str
    game_page_url: str
    id: str
    store_pricing = dict

game_list = []

def wanted_scrape(wanted_url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    wanted_market_page = req.get(wanted_url, headers=hdr)
    soup = bs(wanted_market_page.content,'html.parser')
    links_list = soup.find_all("a", "primary")
    return_list = []

    for item in links_list:
        return_list.append([item.text, item['href'], str(item['href']).split("/")[2]])
        game_list.append(Game(name=item.text, game_page_url=game_page_prefix + item['href'], id= str(item['href']).split("/")[2]))

    wanted_out = game_list

    return wanted_out
