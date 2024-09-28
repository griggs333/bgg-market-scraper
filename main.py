import gradio as gr

from obsolete import api_collections_wanted_list
from _scrapers import scrapers_master


def scraper_main(username):
    wanted_url = "https://boardgamegeek.com/xmlapi2/collection?username=" + username + "&brief=1&wanttobuy=1"
    games_df = api_collections_wanted_list.xml_api_collections(wanted_url)

    bgg_id_list = games_df.index.values.tolist()
    # print(bgg_id_list)

    # gm_listings_df, sellers_df = scrapers_master.gm_listings_page_scraper(bgg_id_list)
    # print(gm_listings_df.index.values.tolist())
    # print(sellers_df.index.values.tolist())
    ms_listings_df = scrapers_master.bgg_page_scraper(bgg_id_list)
    price_history_df = scrapers_master.price_history_scraper(bgg_id_list)
    # a, b = bgg_page_scraper.bgg_page_scraper(bgg_id_list)
    # print(a)
    # print(b)
    return ms_listings_df, price_history_df

demo = gr.Interface(
    fn=scraper_main,
    inputs=["text"],
    outputs=["dataframe", "dataframe"]
)

demo.launch()
