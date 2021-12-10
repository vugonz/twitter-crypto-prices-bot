import requests
import tweepy
import os
from datetime import datetime

client = tweepy.Client(os.environ.get('BEARER'), os.environ.get('CONSUMER_TOKEN'), os.environ.get('CONSUMER_TOKEN_SECRET'), os.environ.get('ACESS_TOKEN'), os.environ.get('ACESS_TOKEN_SECRET'))

time = datetime.now().strftime('%H:%M')
# Courtesy of this amazing repository https://github.com/chubin/rate.sx
# Currently set to get unit price of ADA Cardano in euros
price = float(requests.get('http://eur.rate.sx/1ADA').text)

with open('log.txt', 'a+') as file:
    file.seek(0, 0)
    logs = list(file.readlines())
    file.seek(0, 2)
    file.write('{} {}\n'.format(price, datetime.now().strftime('%c')))
    try:
        prev_price = float(logs[-1].split()[0])
        diff = prev_price - price
    except IndexError:
        diff = 0

#client.create_tweet(text=('ADA is at {:.2f}€ | {}€ GMT\n{:.2f} difference from previous record'.format(price, time, diff)))

