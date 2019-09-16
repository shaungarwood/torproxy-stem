from time import sleep

import requests
from stem import Signal
from stem.control import Controller

import tor


def get_ip(proxies=None, headers=None):
    r = requests.get("http://icanhazip.com", proxies=proxies, headers=headers)
    print (r.text)


proxies = {
  "http": "http://127.0.0.1:8118"
}

headers = {
  'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_1) AppleWebKit/537.73.11 (KHTML, like Gecko) Version/7.0.1 Safari/537.73.11'
}

get_ip()
get_ip(proxies, headers)
for x in range(0,5):
    tor.change_ip()
    sleep(10)
    get_ip(proxies, headers)
