from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup as bs
import pandas as pd

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://boardgamegeek.com/market/browse?objecttype=thing&objectid=67877&pageid=1&currency=any&country=any&sort=recent")
    soup = bs(page.content(), 'html.parser')

    # print(soup.find_all('div',"list-item ng-binding ng-scope"))



    browser.close()