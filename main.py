import gradio as gr
from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd
import aiohttp
from dataclasses import dataclass
import json

import apicall

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

# Create structured pandas dataframes

# Games DF
# games_df = pd.DataFrame({'bgg_id', 'title', 'bgg_page_url', 'sell_price_range'})

# Major Store Listings
major_store_listings_df = pd.DataFrame({'msl_id', 'store_name', 'msl_page_url', 'price'})


# def add_wanted_games(api_ret_dict):
#     games_df = pd.DataFrame.from_dict(api_ret_dict, orient='index')
#     # columns=['title', 'bgg_page_url', 'sell_price_range'])
#     print(games_df)
#
#     return games_df



url = "https://boardgamegeek.com/collection/user/griggs333?rankobjecttype=subtype&rankobjectid=1&columns=title%7Cstatus%7Cversion%7Crating%7Cbggrating%7Cplays%7Ccomment%7Ccommands&geekranks=Board+Game+Rank&wanttobuy=1&objecttype=thing&ff=1&subtype=boardgame"

def game_page_scraper(game_list):
    return_list = []
    hdr = {'User-Agent': 'Mozilla/5.0'}

    for game in game_list:
        game_page = req.get(game.game_page_url, headers=hdr)
        soup = bs(game_page.content, 'html.parser')



def scraper_main(wanted_url):
    # wanted_list = wanted_scrape(wanted_url)
    # game_deets = game_page_scraper(wanted_list)
    games_df = apicall.xml_api_collections(wanted_url)
    temp_out = games_df

    return temp_out

demo = gr.Interface(
    fn=scraper_main,
    inputs=["text"],
    outputs=["dataframe"]
)

demo.launch()
