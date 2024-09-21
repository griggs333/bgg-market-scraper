import time
from bs4 import BeautifulSoup as bs
import requests

# url = "https://boardgamegeek.com/xmlapi2/collection?username=griggs333&brief=1&wanttobuy=1"


def xml_api_collections(url):
    api_ret_dict = {}
    payload = {}
    headers = {
      'Accept-Language': ''
    }

    retry_limit = 3
    retries = 0
    response_code = 0

    while retries < retry_limit:
        response = requests.request("GET", url, headers=headers, data=payload)
        if response.status_code == 200:
            break
        else:
            retries += 1
            print("Returned " + str(response.status_code) + " status code. Will retry in 30 sec. \
                  Retry #" + str(retries) + ". Retry Limit is " + str(retry_limit))
            time.sleep(30)

    if retries == retry_limit:
        raise TimeoutError

    soup = bs(response.content, 'xml')

    wanted_list = soup.find_all('item')
    for item in wanted_list:
        bgg_id = item.attrs['objectid']
        api_ret_dict[bgg_id] = {
                'title': item.text.strip(),
                'bgg_page_url': 'https://boardgamegeek.com/boardgame/' + bgg_id,
                'sell_price_range': ''
                }
    api_ret_df = pd.DataFrame.from_dict(api_ret_dict, orient='index')

    return api_ret_df




#THING API Call below. Not sure if I want to use

# thing_url = "https://boardgamegeek.com/xmlapi2//thing?id=143741&marketplace=1"
#
# retry_limit = 3
# retries = 0
# response_code = 0
#
# while retries < retry_limit:
#     response = requests.request("GET", thing_url, headers=headers, data=payload)
#     if response.status_code == 200:
#         break
#     else:
#         retries += 1
#         print("Returned " + str(response.status_code) + " status code. Will retry in 30 sec. \
#               Retry #" + str(retries) + ". Retry Limit is " + str(retry_limit))
#         time.sleep(30)
#
# if retries == retry_limit:
#     raise TimeoutError
#
# print(response.text)
# print(response.headers['content-type'])
