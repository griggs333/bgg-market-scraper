from _scrapers import geekdo_api_caller, trade_rating_page_scraper
from datetime import datetime, timedelta
import pandas as pd


def bgg_page_scraper(bgg_id_list):
    ms_listings_dict = {}

    for bgg_id in bgg_id_list:
        ms_api_url = geekdo_api_caller.ApiUrl(endpoint_type='major_stores', objectid=bgg_id)
        ms_item_json = geekdo_api_caller.geekdo_api_call(ms_api_url)

        for store in ms_item_json.get('affiliate_ads', []):
            if store['id'] not in ms_listings_dict.keys():
                ms_listings_dict[store['id']] = {
                    'bgg-id': bgg_id,
                    'store_name': store.get('advertiser', {}).get('name', ''),
                    'listing_url': f"https://boardgamegeek.com/{store.get('redirect_url', '')}",
                    'price': store.get('price', ''),
                    'currency': store.get('currency', '')
                }
    ms_listings_df = pd.DataFrame.from_dict(ms_listings_dict, orient='index')

    return ms_listings_df


# def gm_item_page_scraper(listing_id_list):
#     gm_item_dict = {}
#
#     for listing_id in listing_id_list:
#         gm_item_api_url = geekdo_api_caller.ApiUrl(endpoint_type='marketplace_item', objectid=listing_id)
#         gm_item_json = geekdo_api_caller.geekdo_api_call(gm_item_api_url)
#
#         if gm_item_json['productid'] not in gm_item_dict.keys():
#             gm_item_dict[gm_item_json['productid']] = {
#             'bgg-id': ;;;,
#             'Desc'
#             }
#
#
#     return gm_item_df


def gm_listings_page_scraper(bgg_id_list):
    gm_listings_dict = {}
    sellers_dict = {}
    for bgg_id in bgg_id_list:
        gm_listings_api_url = geekdo_api_caller.ApiUrl(endpoint_type='market', objectid=bgg_id, sort="lowprice")
        gm_listings_json = geekdo_api_caller.geekdo_api_call(gm_listings_api_url)

        # Figure out how to deal with pagination - starts at 50/page I think

        for product in gm_listings_json.get('products', []):
            if product['productid'] not in gm_listings_dict.keys():
                gm_listings_dict[product['productid']] = {
                    'bgg-id': product['objectid'],
                    'title': product.get('objectlink', {}).get('name', ''),
                    'desc': product.get('version', {}).get('name', ''),
                    'listing_item_url': "https://boardgamegeek.com" + product.get('producthref', ''),
                    'price': product.get('price', ''),
                    'condition': product.get('condition', ''),
                    'seller_username': product.get('linkeduser', {}).get('username', ''),
                    'shipping_zip': '',
                    'shipping_cost': '',
                    'notes': product.get('linkeduserGeekMarket', {}).get('itemsig', '')
                }
            if product.get('linkeduser', {}).get('userid') not in sellers_dict.keys():
                trade_rating = trade_rating_page_scraper(product.get('linkeduser', {}).get('userid'))

                sellers_dict[product.get('linkeduser', {}).get('userid')] = {
                    'username': product.get('linkeduser', {}).get('username', ''),
                    'user_page_url': product.get('linkeduser', {}).get('canonical_link', ''),
                    'users_listings_url': f"https://boardgamegeek.com/market/{product.get('linkeduser', {}).get('href', '')}",
                    'city': product.get('linkeduser', {}).get('city', ''),
                    'state': product.get('linkeduser', {}).get('state', ''),
                    'country': product.get('linkeduser', {}).get('country', ''),
                    'shipping_zip': '',
                    'num_of_sales': product.get('linkeduserGeekMarket', {}).get('totalsales', ''),
                    'trade_rating': trade_rating,
                    'notes': product.get('linkeduserGeekMarket', {}).get('itemsig', '')
                }

    gm_listings_df = pd.DataFrame.from_dict(gm_listings_dict, orient='index')
    sellers_df = pd.DataFrame.from_dict(sellers_dict, orient='index')

    return gm_listings_df, sellers_df


def price_history_scraper(bgg_id_list):
    price_history_dict = {}

    for bgg_id in bgg_id_list:
        price_history_api_url = geekdo_api_caller.ApiUrl(endpoint_type='price_history', objectid=bgg_id)
        price_history_json = geekdo_api_caller.geekdo_api_call(price_history_api_url)

        for listing in price_history_json.get('items', []):
            sale_date = datetime.strptime(listing['saledate'].split(' ')[0], '%Y-%m-%d')
            recency_interval = timedelta(days=730)
            if listing['itemid'] not in price_history_dict.keys() and datetime.now() > sale_date + recency_interval:
                price_history_dict[listing['itemid']] = {
                    'bgg-id': bgg_id,
                    'history_url': f"https://boardgamegeek.com/market/pricehistory/thing/{bgg_id}",
                    'price': listing.get('price', ''),
                    'currency': listing.get('currency', ''),
                    'condition': listing.get('condition', ''),
                    'sale_date': sale_date.strftime('%m-%d-%Y')
                }

    price_history_df = pd.DataFrame.from_dict(price_history_dict, orient='index')

    return price_history_df
