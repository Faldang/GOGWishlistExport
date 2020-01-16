import requests
import time
import datetime
import csv
import urllib.request


def getuserid(name):
    # Open wishlist based on profile name and turn into string
    wurl = 'https://www.gog.com/u/' + name + '/wishlist'
    fid = urllib.request.urlopen(wurl)
    webpage = fid.read().decode('utf-8')
    # Find where the ID starts and prepare to get the ID
    index = webpage.find('userInfo":{"id":"') + 17
    tid = ''
    # Iterate through the page until you hit the end of the ID
    while True:
        if webpage[index] == '"':
            break
        tid += webpage[index]
        index += 1
    return tid


def onepage():
    # Get page, iterate through products, get discount, amount and title, add to CSV
    r1 = requests.get(url, params=payload)
    time.sleep(1)
    rj1 = r1.json()
    lg = len(rj1['products'])
    for i in range(lg):
        if rj1['products'][i]['isDiscounted']:
            disc = rj1['products'][i]['price']['discountPercentage']
            amo = rj1['products'][i]['price']['amount']
            name = rj1['products'][i]['title']
            name = name.replace(',', '')  # fix for removing commas which mess up the CSV import
            root.writerow([name, disc, amo])
    # Instead of a progress bar, print timestamp once each page is done
    print(payload['page'] + ' ' + str(datetime.datetime.now()))


def site(tn):
    # Iterate through the pages and call onepage to process each one
    for i in range(1, tn + 1):
        payload['page'] = str(i)
        onepage()


def get_conf():
    # Get the user ID for the URL and the file path, from a provided text file
    file = open('dudeId.txt', 'r')
    ret_name = file.readline().rstrip('\n')  # First line is ID
    ret_path = file.readline()  # Second line is file path
    file.close()
    return ret_name, ret_path


# Prepare: Config, Url, Params, Get first page json, Get total number of pages, open file, write CSV header
f_name, f_path = get_conf()
f_id = getuserid(f_name)
url = 'https://www.gog.com/public_wishlist/' + f_id + '/search'
payload = {'hiddenFlag': '0', 'mediaType': '0', 'sortBy': 'title', 'page': '1'}
r = requests.get(url, params=payload)
time.sleep(1)
rj = r.json()
total = rj['totalPages']
f = open(f_path + 'wishlist.csv', 'w', encoding='utf-8', newline='')
root = csv.writer(f)
root.writerow(['Name', 'Discount', 'Amount'])
site(total)
f.close()

# https://www.gog.com/public_wishlist/975863384196/search?hiddenFlag=0&mediaType=0&page=1&sortBy=title

if __name__ == '__main__':
    print('done')
