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
        #content = [ {'row':int(line[:6].replace('F','0').replace('B','1'),2),'col':int(line[7:].replace('L','0').replace('R','1'),2)} for line in f]
        content = [ {'row':int(line[:7].replace('F','0').replace('B','1'),2),'col':int(line[7:].replace('L','0').replace('R','1'),2)} for line in f]
print(content)
maxId = 0
for seat in content:
    if maxId < seat['row'] * 8 + seat['col']:
        maxId = seat['row'] * 8 + seat['col']
print(maxId)
