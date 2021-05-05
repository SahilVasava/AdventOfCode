import urllib.request
from copy import deepcopy
from itertools import product
from simplejson import dumps

req = True 
content = []
if req:
    url = 'https://adventofcode.com/2020/day/11/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    content = [ [col for col in row.strip()] for row in content.strip().split('\n')  ] 
else:
    with open('input.txt') as f:
        content = [ [col for col in row.strip()] for row in f.readlines()]
print(f'Initial state: \n {content}')


def getE(i,j):
    if i >= 0 and i < len(content) and j >= 0 and j < len(content[0]):
        return content[i][j]
    else:
        return 'null'


def isEmpty(i,j):
    if content[i][j] == 'L' and getE(i,j+1) != '#' and getE(i+1,j)  != '#'  and getE(i,j-1) != '#' and getE(i-1,j) != '#' and getE(i-1,j+1) != '#' and getE(i+1,j+1) != '#'  and getE(i+1,j-1) != '#' and getE(i-1,j-1) != '#':
        return True


def isOccupied(i,j):
#    print(f'isOccupied: ({i},{j}) = {content[i][j]}')
    if content[i][j] != '#':        
        return False
    x = [i-1,i,i+1]
    y = [j-1,j,j+1]
#    comb = [p for p in product(x,y)]
    count = 0
    for k,l in product(x,y):
        if i == k and j == l:
            continue
#        print(f'\t ({k},{l}) = {getE(k,l)}')
        if getE(k,l) == '#':
            count += 1
        if count >= 4:
            return True
#    print(f'For ({i},{j}) count is {count}')
    return False

while True:
#for ii in range(2):
    temp = deepcopy(content)
    for i,row in enumerate(content):
        for j,col in enumerate(row):
            if isEmpty(i,j):
                temp[i][j] = '#'
            elif isOccupied(i,j):
                temp[i][j] = 'L'
    print(f'\n\nNew state: \n{temp}')
    if dumps(content) == dumps(temp):
        break
    content = temp
#    break
print('\n\n\nFinal state:')
print(content)
print(dumps(content).count('#'))
