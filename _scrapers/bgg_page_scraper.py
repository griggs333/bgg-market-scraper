from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import pandas as pd

def bgg_page_scraper(bgg_id_list):
    gm_listings_dict = {}
    # major_store_listings_df = pd.DataFrame({'msl_id', 'store_name', 'msl_page_url', 'price'})
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page()
        for bgg_id in bgg_id_list:
            page.goto("https://boardgamegeek.com/boardgame/" + str(bgg_id) + "/")
            soup = bs(page.content(), 'html.parser')
            # items = page.evaluate('li.summary-item.summary-sale-item', elements => {return elements})
            # items = page.get_by_role("listitem")
            # items = page.locator('li.summary-item.summary-sale-item')
            items = page.locator('div.summary-sale-item-price').get_by_role("strong")

            print(items.all_text_contents())
            # for item in items.all():
            #     print(item.all_text_contents())


            list_items = soup.find_all('li', "summary-item summary-sale-item ng-scope")
            # print("list items length: " + str(len(list_items)))

            # list_items = soup.select('span.ng-binding')

            print(list_items)

            for item in list_items:
               gm_listings_dict[item.find(class_='list-item-title').a.get('href')[16:]] = {
                'bgg-id': bgg_id,
                'store_name': item.find(class_='list-item-title').text.strip(),
                'msl_page_url': desc,
                'price': "https://boardgamegeek.com" + item.find(class_='list-item-title').a.get('href')
                }



        browser.close()

    gm_listings_df = pd.DataFrame.from_dict(gm_listings_dict, orient='index')

    return gm_listings_df


# gm_listings_page_scraper(['143741'])
# page.goto("https://boardgamegeek.com/boardgame/3955"