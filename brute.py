import string
from itertools import combinations_with_replacement
from tqdm import tqdm
import grequests
import requests

base = 'https://puzzle.menlohacks.com/ditrwe'
chars = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!"#$%&\'()*+,-./:;<=>?@[\\]^_`{|}~'

for x in tqdm(chars):
    if requests.get(base + x).status_code == 200:
        print(x)
exit()

l = 1
while True:
    urls = combinations_with_replacement(chars, l)
    # print(list(urls))
    rs = (grequests.get(base + ''.join(u)) for u in urls)
    for x in tqdm(grequests.map(rs)):
        if x.status_code != 404:
            # print(vars(x))
            print(x.url[x.url.rfind('/'):])
    print(f'done with length {l}')
    l += 1
