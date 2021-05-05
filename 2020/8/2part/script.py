import urllib.request
from copy import deepcopy

req = True 
content = []
if req:
    url = 'https://adventofcode.com/2020/day/8/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    content = [ code for code in content.strip().split('\n')  ] 
else:
    with open('input.txt') as f:
        content = [ code for code in f.readlines()]

content = [ [c.split()[0],c.split()[1][0],int(c.split()[1][1:]),0] for c in content ]

print(content)

def runp(content2):
    acc = 0
    idx = 0
    while True:
        if idx >= len(content2):
            return (True,acc)
        op, a, arg, visited = content2[idx]
        print(f'Before {op} {a} {arg} {visited}')
        if visited == 1:
            print(f'Ans: {acc}')
            return (False,0)
        content2[idx][3] = 1

        if op == 'nop':
            idx += 1
        elif op == 'acc':
            if a == '+':
                acc += arg 
            else:
                acc -= arg
            idx += 1
        elif op == 'jmp':
            if a == '+':
                idx += arg
            else:
                idx -= arg
        print(f'after {op} {a} {arg} {visited}')

for i, ct in enumerate(content):
    cp = []
    print(f'Loop for i {i} and ct {ct}')
    if ct[0] == 'nop' and ct[2] != 0:
        cp = deepcopy(content)
        cp[i][0] = 'jmp'
        print(f'content: {content} \n cp : {cp}')
    elif ct[0] == 'jmp':
        cp = deepcopy(content)
        cp[i][0] = 'nop'
        print(f'content: {content} \n cp : {cp}')
    else:
        continue
    res = runp(cp)
    print("Returned!!!!!")
    if res[0]:
        print(f'Found the bug!!!! At: {i} {ct} {res[1]}')
        break


#runp(content)
