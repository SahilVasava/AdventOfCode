import urllib.request

req = True 
content = []
if req:
    url = 'https://adventofcode.com/2020/day/10/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    content = [ int(code) for code in content.strip().split('\n')  ] 
else:
    with open('input2.txt') as f:
        content = [ int(code) for code in f.readlines()]
print(content)

ones = twos = threes = lastJ = 0
high = max(content)

a =[[0]]
way = 1
while True:
    arr = []
    for ele in content:
        if ele - lastJ <= 3 and ele - lastJ > 0:
            arr.append(ele)
    arr.sort()
    print(arr)
    a.append(arr.copy())
    while len(arr) != 0:
        el = arr.pop(0)
        if el - lastJ == 1:
            ones += 1
        elif el - lastJ == 2:
            twos += 1
        else:
            threes += 1
        lastJ = el
    if lastJ == high:
        threes += 1
        break
print(f'Ones {ones} twos {twos} threes {threes} lastJ {lastJ} mult {ones*threes}')
print(a)

for i,ls in enumerate(a):
    if len(ls) == 2:
        way *=2
        print('way 2')
    elif len(ls) == 3:
        if a[i+1][0] - ls[2] == 1:
            way *=7
            print('way 7')
        elif a[i+1][0] - ls[2] == 2:
            way *=6
            print('way 6')
        elif a[i+1][0] - ls[2] == 3:
            way *=4
            print('way 4')
print(way)
