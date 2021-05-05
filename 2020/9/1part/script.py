import urllib.request

req = True
content = []
if req:
    url = 'https://adventofcode.com/2020/day/9/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    content = [ int(code) for code in content.strip().split('\n')  ] 
else:
    with open('input.txt') as f:
        content = [ int(code) for code in f.readlines()]

#c = content[:25]
#c.sort()
invalid = 0
for i,val in enumerate(content):
    if i+25 >= len(content):
        break
    arr = content[i:i+25]
    arr.sort()
    print(arr)
    valid = False
    print(f'Loop for {content[i+25]}')
    for k,vall in enumerate(arr):
        print(f'Outer Loop for {content[i+25]} {k} {vall}')
        if vall > content[i+25] and valid:
            break
        for valll in arr[k+1:]:
            print(f'Inner Loop for {content[i+25]} {k} {valll}')
            if vall + valll == content[i+25]:
                valid = True
                break
    if not valid:
        print(f'Found invalid {i} {content[i+25]}')
        invalid = content[i+25]
        break

found = False
for i in range(len(content)):
    sum = 0
    a = []
    for jk,num in enumerate(content[i:]):
        sum += num
        a.append(num)
        if sum >= invalid:
            break
    if sum == invalid:
        found = True
        print(f'Found list: {a} {min(a) + max(a)}')
        break
print(found)
