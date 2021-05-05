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


#def getE(i,j):
#    if i >= 0 and i < len(content) and j >= 0 and j < len(content[0]):
#        return content[i][j]
#    else:
#        return 'null'
#
#
#def isEmpty(i,j):
#    if content[i][j] != 'L':
#        return False
#    k = l = 0
#
#    for dr in [-1,0,1]:
#        for dc in [-1,0,1]:
#            if not (dr == 0 and dc ==0):
#                rr = i+dr
#                cc = j+dc
#                while 0<=rr
#    while True:
#        if getE(i,j+l) == 'null' and getE(i+k,j) == 'null'  and getE(i,j-l) == 'null' and getE(i-k,j) == 'null' and getE(i-k,j+l) == 'null' and getE(i+k,j+l) == 'null'  and getE(i+k,j-l) == 'null' and getE(i-k,j-l) == 'null':
#            return True
#        if getE(i,j+l) == '#' or getE(i+k,j) == '#'  or getE(i,j-l) == '#' or getE(i-k,j) == '#' or getE(i-k,j+l) == '#' or getE(i+k,j+l) == '#'  or getE(i+k,j-l) == '#' or getE(i-k,j-l) == '#':
#            return False 
#        k += 1
#        l += 1
#
#
#def isOccupied(i,j):
#    print(f'isOccupied: ({i},{j}) = {content[i][j]}')
#    if content[i][j] != '#':        
#        return False
#    x = [i-1,i,i+1]
#    y = [j-1,j,j+1]
#    count = 0
#    k = l = 0
##    top = bot = left = right = tr = br = bl = tl = False
#    st = set()    
#    while True:
#        if getE(i,j+l) == 'null' and getE(i+k,j) == 'null'  and getE(i,j-l) == 'null' and getE(i-k,j) == 'null' and getE(i-k,j+l) == 'null' and getE(i+k,j+l) == 'null'  and getE(i+k,j-l) == 'null' and getE(i-k,j-l) == 'null':
#            print(f'\tReached limit')
#            return False 
#        if getE(i,j+l) == '#':
#            st.add('right')
#        if getE(i+k,j) == '#':
#            st.add('bot')
#        if getE(i,j-l) == '#':
#            st.add('left')
#        if getE(i-k,j) == '#': 
#            st.add('top')
#        if getE(i-k,j+l) == '#':
#            st.add('tr')
#        if getE(i+k,j+l) == '#':
#            st.add('br')
#        if getE(i+k,j-l) == '#':
#            st.add('bl')
#        if getE(i-k,j-l) == '#':
#            st.add('tl')
#        print(f'Set is {set}')
#
#        if len(st) >= 5:
#            print(f'\tLenght greater than 5 {len(st)} {st}')
#            return True
#
#
##        if getE(i,j+l) == '#' or getE(i+k,j) == '#'  or getE(i,j-l) == '#' or getE(i-k,j) == '#' or getE(i-k,j+l) == '#' or getE(i+k,j+l) == '#'  or getE(i+k,j-l) == '#' or getE(i-k,j-l) == '#':
##            return False 
#        k += 1
#        l += 1

#    for k,l in product(x,y):
#        if i == k and j == l:
#            continue
#        print(f'\t ({k},{l}) = {getE(k,l)}')
#        if getE(k,l) == '#':
#            count += 1
#        if count >= 5:
#            return True
#    print(f'For ({i},{j}) count is {count}')
#    return False

while True:
#for ii in range(2):
    temp = deepcopy(content)
    change = False
    R = len(content)
    C = len(content[0])
    for r in range(R):
        for c in range(C):
            nocc = 0
            for dr in [-1,0,1]:
                for dc in [-1,0,1]:
                    if not (dr == 0 and dc == 0):
                        rr = r+dr
                        cc = c+dc
                        while 0<=rr<R and 0<=cc<C and content[rr][cc] == '.':
                            rr = rr+dr
                            cc = cc+dc
                        if 0<=rr<R and 0<=cc<C and content[rr][cc] == '#':
                            nocc += 1
            if content[r][c] == 'L':
                if nocc == 0:
                    temp[r][c] = '#'
                    change = True
            elif content[r][c] == '#' and nocc>=5:
                temp[r][c] = 'L'
                change = True
    print(f'\n\nNew state: \n{temp}')
    if not change:
        break
    content = temp
#    break
print('\n\n\nFinal state:')
print(content)
print(dumps(content).count('#'))
