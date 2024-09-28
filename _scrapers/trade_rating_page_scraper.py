from bs4 import BeautifulSoup as bs
import requests as req


def trade_rating_scraper(userid):

    url = f"https://boardgamegeek.com/trade/feedback/{userid}"
    response = req.get(url)
    soup = bs(response.content, 'lxml')

    positive_count = soup.find_all('td', 'positive')
    negative_count = soup.find_all('td', 'negative')

    trade_rating = f"+{positive_count}/-{negative_count}"

    return trade_rating
