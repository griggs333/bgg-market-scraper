import requests as req
import json


class ApiUrl:
    def __init__(self, endpoint_type, objectid, ajax='1', browsetype='browse', colluserid='0',
                 condition='any', country='US', currency='USD', displaymode='list',
                 findmywants='0', inventorytype='any', marketdomain='boardgame',
                 nosession='1', objecttype='thing', pageid='1', productstate='active',
                 shiparea='usa', sort='lowprice', stock='instock', userid='0', context='gameoverview'):
        ### Required
        self.endpoint_type = endpoint_type
        self.objectid = objectid
        ###

        self.ajax = ajax
        self.browsetype = browsetype
        self.colluserid = colluserid
        self.condition = condition
        self.country = country
        self.currency = currency
        self.displaymode = displaymode
        self.findmywants = findmywants
        self.inventorytype = inventorytype
        self.marketdomain = marketdomain
        self.nosession = nosession
        self.objecttype = objecttype
        self.pageid = pageid
        self.productstate = productstate
        self.shiparea = shiparea
        self.sort = sort
        self.stock = stock
        self.userid = userid
        self.context = context


"""
marketplace = url = "https://api.geekdo.com/api/market/products?ajax=1&browsetype=browse&colluserid=0&condition=any&country=US&currency=USD&displaymode=list&findmywants=0&inventorytype=any&marketdomain=boardgame&nosession=1&objectid=3955&objecttype=thing&pageid=1&productstate=active&shiparea=usa&sort=recent&stock=instock&userid=0"
    ajax=1
    browsetype=browse
    colluserid=0
    condition=any
    country=any
    currency=any
    displaymode=list
    findmywants=0
    inventorytype=any
    marketdomain=boardgame
    nosession=1
    objectid=3955
    objecttype=thing
    pageid=1
    productstate=active
    shiparea=any
    sort=recent
    stock=instock
    userid=0

major_stores = https://api.geekdo.com/api/affiliateads?context=gameoverview&objectid=3955&objecttype=thing')
    context=gameoverview
    objectid=3955
    objecttype=thing

marketplace_item = https://api.geekdo.com/api/market/products/3531516

price_history = https://boardgamegeek.com/api/market/products/pricehistory?ajax=1&condition=any&currency=USD&objectid=3955&objecttype=thing&pageid=1
    ajax=1
    condition=any
    currency=USD
    objectid=3955
    objecttype=thing
    pageid=1

"""

def geekdo_api_call(apiURL):

    if apiURL.endpoint_type == "market":

        url = (f'https://api.geekdo.com/api/market/products?ajax={apiURL.ajax}'
        f'&browsetype={apiURL.browsetype}&colluserid={apiURL.colluserid}&condition={apiURL.condition}'
        f'&country={apiURL.country}&currency={apiURL.currency}&displaymode={apiURL.displaymode}'
        f'&findmywants={apiURL.findmywants}&inventorytype={apiURL.inventorytype}'
        f'&marketdomain={apiURL.marketdomain}&nosession={apiURL.nosession}&objectid={apiURL.objectid}'
        f'&objecttype={apiURL.objecttype}&pageid={apiURL.pageid}&productstate={apiURL.productstate}'
        f'&shiparea={apiURL.shiparea}&sort={apiURL.sort}&stock={apiURL.stock}&userid={apiURL.userid}')

    elif apiURL.endpoint_type == "major_stores":

        url = (f'https://api.geekdo.com/api/affiliateads?context={apiURL.context}'
        f'&objectid={apiURL.objectid}&objecttype={apiURL.objecttype}')

    elif apiURL.endpoint_type == "marketplace_item":

        url = f"https://api.geekdo.com/api/market/products/{apiURL.objectid}"


    elif apiURL.endpoint_type == "price_history":

        url = (f'https://boardgamegeek.com/api/market/products/pricehistory?ajax={apiURL.ajax}'
        f'&condition={apiURL.condition}&currency={apiURL.currency}&objectid={apiURL.objectid}'
        f'&objecttype={apiURL.objecttype}&pageid={apiURL.pageid}')

    else:
        raise "Bad endpoint type given"

    response = req.get(url)

    json_data = json.loads(response.content)
    # print(url)
    return json_data