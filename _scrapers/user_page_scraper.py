from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import pandas as pd

def user_page_scraper(wanted_list):
    gm_listings_dict = {}
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for game in wanted_list:
            page.goto("https://boardgamegeek.com/market/browse?objecttype=thing&objectid=" + str(game) + "&pageid=1&currency=USD&country=US&&shiparea=usa")
            soup = bs(page.content(), 'html.parser')

            list_items = soup.find_all('div',"list-item ng-binding ng-scope")
            print("list items legnth: " + str(len(list_items)))

            for item in list_items:
                if item.find(class_='list-item-description') == None:
                    desc = ''
                else:
                    desc = item.find(class_='list-item-description').text.strip()

                gm_listings_dict[item.find(class_='list-item-title').a.get('href')[16:]] = {
                    'bgg-id': game,
                    'title': item.find(class_='list-item-title').text.strip(),
                    'desc': desc,
                    'listing_item_url': "https://boardgamegeek.com" + item.find(class_='list-item-title').a.get('href'),
                    'price': item.find(class_='list-item-price').text.strip(),
                    'condition': item.find(class_='list-item-condition').text.strip(),
                    'seller_username': item.find(class_='list-item-seller').text.strip(),
                    'shipping_zip': '',
                    'shipping_cost': '',
                    'notes': ''
                }



        browser.close()

    gm_listings_df = pd.DataFrame.from_dict(gm_listings_dict, orient='index')

    return gm_listings_df


# gm_listings_page_scraper(['143741'])