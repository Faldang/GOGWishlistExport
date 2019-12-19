import requests
import time
import datetime
import csv


def onepage():
    r1 = requests.get(url, params=payload)
    time.sleep(1)
    rj1 = r1.json()
    lg = len(rj1['products'])
    for i in range(lg):
        if rj1['products'][i]['isDiscounted']:
            disc = rj1['products'][i]['price']['discountPercentage']
            amo = rj1['products'][i]['price']['amount']
            name = rj1['products'][i]['title']
            root.writerow([name, disc, amo])
    print(payload['page'] + ' ' + str(datetime.datetime.now()))


def site(tn):
    for i in range(1, tn+1):
        payload['page'] = str(i)
        onepage()


# Prepare: Url, Params, Get first page json, Get total number of pages, open file
url = 'https://www.gog.com/public_wishlist/975863384196/search'
payload = {'hiddenFlag': '0', 'mediaType': '0', 'sortBy': 'title', 'page': '1'}
r = requests.get(url, params=payload)
time.sleep(1)
rj = r.json()
total = rj['totalPages']
f = open('wishlist.csv', 'w', encoding='utf-8')
root = csv.writer(f)
root.writerow(['Name', 'Discount', 'Amount'])
site(total)
f.close()

# https://www.gog.com/public_wishlist/975863384196/search?hiddenFlag=0&mediaType=0&page=1&sortBy=title

if __name__ == '__main__':
    print('done')
