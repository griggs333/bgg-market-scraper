import time
from bs4 import BeautifulSoup as bs
import requests

url = "https://boardgamegeek.com/xmlapi2/collection?username=griggs333&brief=1&wanttobuy=1"

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

print(response.text)
print(response.headers['content-type'])


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
