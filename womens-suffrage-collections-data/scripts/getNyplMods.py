import requests
import configparser
from lxml import etree as ET
#import xml.etree.ElementTree as ET
import time
import mods2csv
import sys

#function to query MODS -- query = 'search string', field = 'mods field' (leave empty to search entire record)
def search(query, field=''):
    url = base + 'items/search.json'
    payload = {'q':query, 'field':field}
    call = requests.get(url, params=payload, headers={'Authorization': auth})
    return call.json()

#function to get captures for a given UUID
def getCaptures(uuid, titles='yes'):
    url = base + 'items/' + uuid + '?per_page=10000'
    if titles == 'yes':
        url = url + '&withTitles=yes'
    call = requests.get(url, headers={'Authorization': auth})
    return call.json()

#function to get the MODS XML for a given UUID
def getMODS(uuid, dataformat='.xml'):
    url = base + 'mods/' + uuid + dataformat
    call = requests.get(url, headers={'Authorization': auth})
    return call

def getCaptureDetails(uuid, dataformat='.xml'):
    url = base + 'items/item_details/' + uuid + dataformat
    call = requests.get(url, headers={'Authorization': auth})
    return call    

#function to get all MODS info and first capture thumbnails for items in an NYPL collection
def getItemsAndImages(uuid):
    response = getCaptures(uuid, titles='no')
    captures = response['nyplAPI']['response']['capture']
    items = []
    for c in captures:
        capturedetails = getCaptureDetails(c['uuid'])
        root = ET.fromstring(capturedetails.content)
        sibs = root.findall('./response/sibling_captures/capture')
        for s in sibs:
            if (c['uuid'] == s.find('./uuid').text) and (s.find('./orderInSequence').text == '1'):
                item = {}
                item['uuid'] = c['uuid']
                item['imageid'] = s.find('./imageID').text
                item['thumbnail'] = 'http://images.nypl.org/index.php?t=b&id=' + item['imageid']
                item['image'] = 'http://images.nypl.org/index.php?t=r&id=' + item['imageid']
                item['link'] = s.find('./itemLink').text
                item['mods'] = ET.tostring(root.find('./response/mods'))
                item['primary_id'] = root.findall('./response/mods/identifier[@type="uuid"]')[0].text
                items.append(item)
    return items

if __name__ == "__main__":
    #take uuid from first argument of command as collection uuid
    coll_uuid = sys.argv[1]
    
    #create an instance of configparser, then read your config file into it
    config = configparser.ConfigParser()
    config.read('config.ini')
    #find your DC token in the config file content (by section and name) and assign it to a variable
    token = config.get('DC','token')
    #saving the base url in your config file will make it easier to find next time you want to use it
    base = config.get('DC', 'base')
    #now you're ready to put together your API calls
    auth = 'Token token=' + token
    
    #get the items and images for a given collection uuid and output a csv file
    coll = getItemsAndImages(coll_uuid)
    #create output file and csvwriter
    filename = "nypl" + coll_uuid + '.csv'
    f = open(filename, 'wb')
    writer = mods2csv.csvSetup(f)
    for c in coll:
        mods2csv.modsToRow(c, 'NYPL', writer)
    f.close()