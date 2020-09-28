import grequests
from tqdm import tqdm

with open('64.txt', 'r') as f:
    s = f.read().split('\n')
base = 'https://puzzle.menlohacks.com/'

rs = (grequests.get(base + u) for u in s)
for x in tqdm(grequests.map(rs)):
    print(x.status_code, x.url)