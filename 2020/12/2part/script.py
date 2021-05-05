import urllib.request

req = True 
content = []
if req:
    url = 'https://adventofcode.com/2020/day/12/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    content = [ (row.strip()[0],int(row.strip()[1:])) for row in content.strip().split('\n')  ] 
else:
    with open('input.txt') as f:
        content = [ (row.strip()[0],int(row.strip()[1:])) for row in f.readlines()]

print(f'{content}')

dirs = ['N','E','S','W']
cur = 'E'
route = [(0,0)]
idx = 1
waypt = [10,1]

def move(dirr,dist):
    
    if dirr == 'N':
        last = route[-1]
        route.append((last[0],last[1]+dist))
    elif dirr == 'S':
        last = route[-1]
        route.append((last[0],last[1]-dist))
    elif dirr == 'E':
        last = route[-1]
        route.append((last[0]+dist,last[1]))
    elif dirr == 'W':
        last = route[-1]
        route.append((last[0]-dist,last[1]))


for inst in content:
    act = inst[0]
    val = inst[1]
    
    if act == 'L':
        idx = (idx - int(val/90)) % 4
        cur = dirs[idx]
    elif act == 'R':
        idx = (idx + int(val/90)) % 4
        cur = dirs[idx]
    elif act == 'F':
        move(cur,val)
    else:
        move(act,val)

mDist = abs(route[-1][0]-route[0][0]) + abs(route[-1][1] -route[0][1])
print(route)
print(f'Manhatten dist: {mDist}')
