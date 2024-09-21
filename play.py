from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import pandas as pd

df = pd.DataFrame()
with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://boardgamegeek.com/market/browse?objecttype=thing&objectid=143741&pageid=1&currency=USD&country=US&&shiparea=usa")
    soup = bs(page.content(), 'html.parser')

    list_items = soup.find_all('div',"list-item ng-binding ng-scope")

    for item in list_items:




    browser.close()