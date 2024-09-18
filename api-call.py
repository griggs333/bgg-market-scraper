import requests

url = "https://boardgamegeek.com/xmlapi2/collection?username=griggs333&brief=1&wanttobuy=0"

payload = {}
headers = {
  'Accept-Language': ''
}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
