import urllib.request

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
acc = 0
#for inst in content:
idx = 0
while True:
    op, a, arg, visited = content[idx]
    print(f'Before {op} {a} {arg} {visited}')
    if visited == 1:
        print(f'Ans: {acc}')
        break
    content[idx][3] = 1

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
