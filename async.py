import gradio as gr
from bs4 import BeautifulSoup as bs
import requests as req
import aiohttp
import asyncio
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

async def main():

    async with aiohttp.ClientSession() as session:
        async with session.get('http://python.org') as response:

            print("Status:", response.status)
            print("Content-type:", response.headers['content-type'])

            html = await response.text()
            print("Body:", html[:15], "...")
asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
asyncio.run(main())