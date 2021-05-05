import urllib.request
import re

#patt = re.compile()
req = True 
content = []
stop = ['contain', 'bag', 'bags', 'bag.', 'bags.', 'bag,', 'bags,']
if req:
    url = 'https://adventofcode.com/2020/day/7/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    #content = [ {' '.join([[word for word in rule.split() if word not in stop][0],[word for word in rule.split() if word not in stop][1]]):[word for word in rule.split() if word not in stop][2:]} for rule in content.strip().split('\n') ]
    content = { ' '.join([[word for word in rule.split() if word not in stop][0],[word for word in rule.split() if word not in stop][1]]):[word for word in rule.split() if word not in stop][2:] for rule in content.strip().split('\n') }
else:
    with open('input.txt') as f:
        #content = [ {'row':int(line[:6].replace('F','0').replace('B','1'),2),'col':int(line[7:].replace('L','0').replace('R','1'),2)} for line in f]
        content = [ {'row':int(line[:7].replace('F','0').replace('B','1'),2),'col':int(line[7:].replace('L','0').replace('R','1'),2)} for line in f]

for key, val in content.items():
    arr = []
    for i in range(0,int(lenn := len(val)),3):    
        if lenn % 3 == 0:
            first = val[i+1]
            second = val[i+2]
            arr.append(' '.join([first,second]))
    
    content[key] = arr 
#    print(key,val,arr)


def search(term):
    for k,v in content.items():
        #print(k,v)
        if term in v:
            print(k,v,term)
            yield from search(k)
    print(term)
    yield term
#print(content)
print(len({i for i in search('shiny gold')})-1)
