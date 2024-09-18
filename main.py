import gradio as gr
from bs4 import BeautifulSoup as bs
import requests as req
import aiohttp
from dataclasses import dataclass
import json

# REFERENCE

# Anomia
#
#   Game page = "https://boardgamegeek.com/boardgame/67877/anomia"
#   Geekmarket page = "https://boardgamegeek.com/market/browse?objecttype=thing&objectid=67877&pageid=1&currency=USD&country=US"
#   Price Tracking = "https://boardgamegeek.com/market/pricehistory/thing/67877"
#

game_page_prefix = "https://boardgamegeek.com"
market_prefix = "https://boardgamegeek.com/market/browse?objecttype=thing&objectid="
market_suffix = "&pageid=1&currency=USD&country=US"

@dataclass
class Game:
    name: str
    game_page_url: str
    id: str
    store_pricing = dict

game_list = []

url = "https://boardgamegeek.com/collection/user/griggs333?rankobjecttype=subtype&rankobjectid=1&columns=title%7Cstatus%7Cversion%7Crating%7Cbggrating%7Cplays%7Ccomment%7Ccommands&geekranks=Board+Game+Rank&wanttobuy=1&objecttype=thing&ff=1&subtype=boardgame"

def wanted_scrape(wanted_url):
    hdr = {'User-Agent': 'Mozilla/5.0'}
    wanted_market_page = req.get(wanted_url, headers=hdr)
    soup = bs(wanted_market_page.content,'html.parser')
    links_list = soup.find_all("a", "primary")
    return_list = []

    for item in links_list:
        return_list.append([item.text, item['href'], str(item['href']).split("/")[2]])
        game_list = game_list.append(Game(name=item.text, game_page_url=game_page_prefix + item['href'], id= str(item['href']).split("/")[2]))
    wanted_out = game_list
    return wanted_out

def game_page_scraper(game_list):
    return_list = []
    hdr = {'User-Agent': 'Mozilla/5.0'}

    for game in game_list:
        game_page = req.get(game.game_page_url, headers=hdr)
        soup = bs(game_page.content, 'html.parser')





def scraper_main(wanted_url):
    wanted_list = wanted_scrape(wanted_url)
    game_deets = game_page_scraper(wanted_list)



    return temp_out

demo = gr.Interface(
    fn=scraper_main,
    inputs=["text"],
    outputs=["dataframe"]
)

demo.launch()
