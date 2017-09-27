import csv
import numpy
import yaml

def load_config(config_file):

    with open(config_file, 'r') as ymlfile:
        cfg = yaml.load(ymlfile)

    btc_buy_price = cfg['buy_prices']['btc']
    eth_buy_price = cfg['buy_prices']['eth']

    return(btc_buy_price, eth_buy_price)

def get_last_20min_data(results_file):

    eth_data = []
    btc_data = []

    with open(results_file, 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    for trade in data[-40:]:

        if trade[0] == 'eth_cad':
            eth_data.append(float(trade[1]))

        elif trade[0] == 'btc_cad':
            btc_data.append(float(trade[1]))

        else:
            break

    return(eth_data, btc_data)

def calculate_mean(eth_buy_price, btc_buy_price, eth_data, btc_data):

    eth_mean_20min = numpy.mean(eth_data)
    if eth_mean_20min >= 1.5 * eth_buy_price:
        eth_profit = True
    else:
        eth_profit = False

    btc_mean_20min = numpy.mean(btc_data)
    if btc_mean_20min >= 1.5 * btc_buy_price:
        btc_profit = True
    else:
        btc_profit = False

    return(eth_profit, btc_profit)

def main():

    config_file = 'config.yml'
    results_file = 'last_sell.csv'

    btc_buy_price, eth_buy_price = load_config(config_file)

    eth_data, btc_data = get_last_20min_data(results_file)

    eth_profit, btc_profit = calculate_mean(eth_buy_price, btc_buy_price, eth_data, btc_data)

    return(eth_profit, btc_profit)

if __name__ == '__main__':
    eth_profit, btc_profit = main()
