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


def site(tn):
    # Iterate through the pages and get discount, amount, title and type, add to list
    export_iter = []
    for i1 in range(1, tn + 1):
        payload['page'] = str(i1)
        r1 = requests.get(url, params=payload)
        time.sleep(1)
        rj1 = r1.json()
        lg = len(rj1['products'])
        for x in range(lg):
            # if rj1['products'][x]['isDiscounted']:
            disc = rj1['products'][x]['price']['discountPercentage']
            amo = rj1['products'][x]['price']['amount']
            name = rj1['products'][x]['title']
            item_type = rj1['products'][x]['type']
            name = name.replace(',', '')  # fix for removing commas which mess up the CSV import
            # format is name, discount, amount, type
            export_iter.append([name, disc, amo, item_type])
        # Instead of a progress bar, print timestamp once each page is done
        print(payload['page'] + ' ' + str(datetime.datetime.now()))
    return export_iter


def get_conf():
    # Get the user ID for the URL and the file path, from a provided text file
    file = open('dudeId.txt', 'r')
    ret_name = file.readline().rstrip('\n')  # First line is ID
    ret_path = file.readline()  # Second line is file path
    file.close()
    return ret_name, ret_path


def csv_with_discount(flist):
    # Take full list, open file, set header
    f = open(f_path + 'wishlist.csv', 'w', encoding='utf-8', newline='')
    root = csv.writer(f)
    root.writerow(['Name', 'Discount', 'Amount', 'Type'])
    # Write each row in file
    for i2 in range(len(flist)):
        if flist[i2][1] != 0:
            name = flist[i2][0]
            disc = flist[i2][1]
            amo = flist[i2][2]
            item_type = flist[i2][3]
            root.writerow([name, disc, amo, item_type])
    f.close()


def csv_no_discount(flist):
    # Take full list, open file, set header
    f = open(f_path + 'wishlist.csv', 'w', encoding='utf-8', newline='')
    root = csv.writer(f)
    root.writerow(['Name', 'Amount', 'Type'])
    # Write each row in file
    for i3 in range(len(flist)):
        name = flist[i3][0]
        amo = flist[i3][2]
        item_type = flist[i3][3]
        root.writerow([name, amo, item_type])
    f.close()


# Prepare: Config, userId
f_name, f_path = get_conf()
f_id = getuserid(f_name)

# Prepare: URL, get first page, get total number of pages
url = 'https://www.gog.com/public_wishlist/' + f_id + '/search'
payload = {'hiddenFlag': '0', 'mediaType': '0', 'sortBy': 'title', 'page': '1'}
r = requests.get(url, params=payload)
time.sleep(1)
rj = r.json()
total = rj['totalPages']

# Export a full List of the wishlist, set flag
export = site(total)
export_flag = True
# testflag = False

# Go through the list and if there are any discounted items, make file
for i in range(len(export)):
    # if testflag:
    if export[i][1] != 0:
        export_flag = False
        csv_with_discount(export)
        print("Discount exists, list of discounted items exported")
        break

# If there are no discounted items, make file differently
if export_flag:
    csv_no_discount(export)
    print("No discounts currently, full list exported")

# https://www.gog.com/public_wishlist/975863384196/search?hiddenFlag=0&mediaType=0&page=1&sortBy=title

if __name__ == '__main__':
    print('done')
