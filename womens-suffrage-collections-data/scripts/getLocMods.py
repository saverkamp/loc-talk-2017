import requests
import xml.etree.ElementTree as ET
import time
import mods2csv
import sys

lcbase = 'https://www.loc.gov/collections/'
  
def getLCitems(url, items=[]):
    call = requests.get(url).json()
    results = call['results']
    items = items
    for r in results:
        if 'item_id' in r:
            item = {}
            item['source'] = 'LoC'
            item['primary_id'] = r['item_id']
            item['link'] = r['url']
            item['thumbnail'] = 'http:' + r['image_url'][0]
            item['image'] = 'http:' + r['image_url'][0]
            #get MODS records from lccn
            modsurl = 'http://lccn.loc.gov/' + r['item_id'] + 'mods'
            item['mods'] = requests.get(modsurl).content
            items.append(item)
            time.sleep(7)
    next_page = call["pagination"]["next"] #get the next page url
    if next_page is not None: #make sure we haven't hit the end of the pages
        getLCitems(next_page, items=items)
    return items

if __name__ == "__main__":
    #take collection slug from first argument of command as collection uuid
    coll_id = sys.argv[1]
    url = lcbase + coll_id + '?fo=json'
    #get all items from a collection through api
    coll = getLCitems(url)
    #create output file and csvwriter
    filename = "loc_" + coll_id + '.csv'
    f = open(filename, 'wb')
    writer = mods2csv.csvSetup(f)
    for c in coll:
        mods2csv.modsToRow(c, 'LoC', writer)
    f.close()
    