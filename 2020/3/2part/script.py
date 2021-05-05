import urllib.request
import itertools
import math

req = True
content = []
if req:
    url = 'https://adventofcode.com/2020/day/3/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    data = urllib.request.urlopen(req).read().decode('utf-8')
    content = [ list(str) for str in data.rstrip().split('\n')]
else:
    with open('input.txt') as f:
        content = [ list(str.rstrip()) for str in f]
rows = len(content)
cols =len(content[0])
def init_box(right, down):
    pats = int(math.ceil((right * ( rows  - 1) + 1)/cols))
    #print(f'pats: {pats} rows: {rows} cols: {cols}')
    box = []
    for i in content:
        arr = []
        for j in range(pats):
            arr += i
        box.append(arr)
    #print(f'box rows: {len(box)} cols: {len(box[0])}')
    return box

def traverse_slope(right,down,box):
    count = 0
    rstep = 1
    for k in range(down,rows,down):
        idx = rstep * right
    #    print(len(box[k]),idx)
        if box[k][idx] == '#':
            box[k][idx] = 'x'
            print(f'X: {k},{idx}')
            count += 1
        else:
            box[k][idx] = 'o'
            print(f'O: {k},{idx}')
        rstep += 1
    print(f'Right: {right} Down: {down} Trees: {count}')
    return count
print(traverse_slope(1,1,init_box(1,1))*traverse_slope(3,1,init_box(3,1))*traverse_slope(5,1,init_box(5,1))*traverse_slope(7,1,init_box(7,1))*traverse_slope(1,2,init_box(1,2)))
