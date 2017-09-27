'''
Script to interogate the public Quadriga Coin Exchange API
Documentation: https://www.quadrigacx.com/api_info
'''

import requests, json, csv
from datetime import datetime

def get_exchange_rate(base_url, currency):

    r = requests.get(base_url + currency)

    if r.status_code == 200:

        json_answer = r.json()
        last = json_answer['last']
        unix_timestamp = json_answer['timestamp']
        timestamp = datetime.utcfromtimestamp(float(unix_timestamp)).strftime('%Y-%m-%d %H:%M:%S')

        last_trade = [currency, last, timestamp]

    else:
        
        print('No data available')

    return(last_trade)

def save_to_csv(last_trade):

    with open('last_sell.csv', 'a', newline = '') as f:

        csvwriter = csv.writer(f, delimiter = ',')
        csvwriter.writerow(last_trade)

def main():

    base_url = 'https://api.quadrigacx.com/v2/ticker?book='
    book = ['eth_cad', 'btc_cad']

    for currency in book:

        last_trade = get_exchange_rate(base_url, currency)
        save_to_csv(last_trade)

if __name__ == '__main__':
    main()
