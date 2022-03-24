# scraper.py
import requests
import random
import re
from multiprocessing import Pool
from time import sleep

def handler(proxy):
    """ try to get status of proxy"""
    link = 'http://icanhazip.com'
    myproxies = {'http': f'http://{proxy}',
                 'https': f'https://{proxy}'}
    try:
        response = requests.get(link, proxies=myproxies, timeout=2).text
        print(f'Current proxy {proxy} is working')
        if proxy.split(':')[0] == response.strip():
            with open('valid_proxy2.txt', 'a') as outf:
                outf.write(proxy+'\n')
        valid_proxy.append(response)
    except:
        print(f'Current proxy: {proxy} is down')


""" 1 вариант
with open('valid_proxy.txt') as file:
    proxy_list = ''.join(file.readlines()).split()"""

""" 2 вариант
proxy_base = []
pr_l = (x.strip() for x in open('valid_proxy.txt'))

for i in pr_l:
    proxy_base.append(i)"""
proxy_base = [x.strip() for x in open('valid_proxy.txt')]

if __name__ == '__main__':
    with Pool(4) as process:
        process.map(handler, proxy_base)
