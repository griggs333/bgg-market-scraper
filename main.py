import gradio as gr
from bs4 import BeautifulSoup as bs
import requests as req
import pandas as pd

from _scrapers import api_collections_wanted_list
from _scrapers import bgg_page_scraper
from _scrapers import gm_item_page_scraper
from _scrapers import gm_listings_page_scraper
from _scrapers import historical_pricing_scraper
from _scrapers import trade_rating_page_scraper
from _scrapers import user_page_scraper

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
# major_store_listings_df = pd.DataFrame({'msl_id', 'store_name', 'msl_page_url', 'price'})


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



def scraper_main(username):
    wanted_url = "https://boardgamegeek.com/xmlapi2/collection?username=" + username + "&brief=1&wanttobuy=1"
    games_df = api_collections_wanted_list.xml_api_collections(wanted_url)

    bgg_id_list = games_df.index.values.tolist()
    # print(bgg_id_list)

    gm_listings_df = gm_listings_page_scraper.gm_listings_page_scraper(bgg_id_list)
    major_store_listings_df = bgg_page_scraper.bgg_page_scraper(bgg_id_list)

    return games_df, gm_listings_df

demo = gr.Interface(
    fn=scraper_main,
    inputs=["text"],
    outputs=["dataframe", "dataframe"]
)

demo.launch()
