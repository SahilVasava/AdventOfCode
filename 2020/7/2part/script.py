import urllib.request
import re

#patt = re.compile()
req = False 
content = []
stop = ['contain', 'bag', 'bags', 'bag.', 'bags.', 'bag,', 'bags,']
if req:
    url = 'https://adventofcode.com/2020/day/7/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    content = { ' '.join([[word for word in rule.split() if word not in stop][0],[word for word in rule.split() if word not in stop][1]]):[word for word in rule.split() if word not in stop][2:] for rule in content.strip().split('\n') }
else:
    with open('input.txt') as f:
        content = { ' '.join([[word for word in rule.split() if word not in stop][0],[word for word in rule.split() if word not in stop][1]]):[word for word in rule.split() if word not in stop][2:] for rule in f }

print(content)
for key, val in content.items():
    dic = {} 
    for i in range(0,int(lenn := len(val)),3):    
        if lenn % 3 == 0:
            first = val[i+1]
            second = val[i+2]
            dic[' '.join([first,second])] = val[i]
    
    content[key] = dic
print(content,"\n")

def search_in(term):
    for k,v in content.items():
        if term in v:
            print(k,v,term)
            yield from search_in(k)
    print(term)
    yield term


def search_out(term,mult):
    add = 1 
    for val in content.get(term):
        print(f'prev add = {add}')
        print(f'Term: {term} val: {val}')
        print(f'Prev:  int(content[term][val]: {int(content[term][val])}\n')
        retVal = search_out(val,mult)
        print(f'after: retVal {retVal} int(content[term][val] {int(content[term][val])}')
        add += int(content[term][val])*retVal 
        print(f'after add = {add}\n')
    return add 
print(search_out('shiny gold',1)-1)
