import requests
import time
import datetime


def onepage():
    # Get one page and then iterate through each product and add the title to the file
    r1 = requests.get(url, params=payload)
    time.sleep(1)
    rj1 = r1.json()
    l = len(rj1['products'])
    for i in range(l):
        t1 = rj1['products'][i]['title']
        f.write(t1 + '\n')
    print(payload['page'] + ' ' + str(datetime.datetime.now()))


def site(tn):
    for i in range(1, tn+1):
        payload['page'] = str(i)
        onepage()


# Prepare: Url, Params, Get first page json, Get total number of pages, open file
url = 'https://www.gog.com/games/ajax/filtered'
payload = {'mediaType': 'game', 'sort': 'title', 'page': '1'}
r = requests.get(url, params=payload)
time.sleep(1)
rj = r.json()
total = rj['totalPages']
f = open('file.txt', 'w', encoding='utf-8')
site(total)
f.close()

# print(payload['page'])
# soup object
# rsoup = BeautifulSoup(resp.text, 'html.parser')
# temp = rsoup.find_all(text=True)
# output = ''
# for t in rsoup:
#     output += '{} '.format(t)
# f.write(output)
# f.close()
if __name__ == '__main__':
    print('done')
