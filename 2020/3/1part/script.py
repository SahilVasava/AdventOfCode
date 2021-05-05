import urllib.request
import itertools
import math

url = 'https://adventofcode.com/2020/day/3/input'
headers = {}
headers['Cookie'] = 'session=<token>'

req = urllib.request.Request(url, headers = headers)
content = urllib.request.urlopen(req).read().decode('utf-8')
content = [ list(str) for str in content.rstrip().split('\n')]

right = 3
down = 1
pats = int(math.ceil((right * ( (rows := len(content)) - 1) + 1)/(cols :=len(content[0]))))
#print(f'pats: {pats} rows: {rows} cols: {cols}')
box = []
for i in content:
    arr = []
    for j in range(pats):
        arr += i
    box.append(arr)
#print(f'box rows: {len(box)} cols: {len(box[0])}')
count = 0
for k in range(down,rows,down):
    idx = k * right
#    print(len(box[k]),idx)
    if box[k][idx] == '#':
        box[k][idx] = 'x'
        count += 1
    else:
        box[k][idx] = 'o'

print(count)
