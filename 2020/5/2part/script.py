import urllib.request
import itertools
import math

req = True 
content = []
if req:
    url = 'https://adventofcode.com/2020/day/5/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    content = [ {'row':int(line.replace('F','0').replace('B','1')[:7],2),'col':int(line.replace('L','0').replace('R','1')[7:],2)}  for line in content.strip().split('\n')] 
else:
    with open('input.txt') as f:
        content = [ {'row':int(line[:7].replace('F','0').replace('B','1'),2),'col':int(line[7:].replace('L','0').replace('R','1'),2)} for line in f]
#print(content)
maxId = 0
ids = []
for seat in content:
    ids.append(seat['row'] * 8 + seat['col'])
ids.sort()


def missing_elements(L, start, end):
    if end - start <= 1:
        if L[end] - L[start] > 1:
            yield from range(L[start] + 1, L[end])
        return

    index = start + (end - start) // 2

    # is the lower half consecutive?
    consecutive_low =  L[index] == L[start] + (index - start)
    if not consecutive_low:
        yield from missing_elements(L, start, index)

    # is the upper part consecutive?
    consecutive_high =  L[index] == L[end] - (end - index)
    if not consecutive_high:
        yield from missing_elements(L, index, end)

for idd in ids:
    if idd+1 not in ids and idd+2 in ids:
        print(idd+1)
#print(ids)
#print(list(missing_elements(ids,0,len(ids)-1)))
