import urllib.request

req = True 
content = []
if req:
    url = 'https://adventofcode.com/2020/day/6/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    content = urllib.request.urlopen(req).read().decode('utf-8')
    content = [  len(sett) for sett in [set(u for peep in group.split('\n') for u in peep)  for group in content.strip().split('\n\n')] ]
else:
    with open('input.txt') as f:
        #content = [ {'row':int(line[:6].replace('F','0').replace('B','1'),2),'col':int(line[7:].replace('L','0').replace('R','1'),2)} for line in f]
        content = [ {'row':int(line[:7].replace('F','0').replace('B','1'),2),'col':int(line[7:].replace('L','0').replace('R','1'),2)} for line in f]
print(sum(content))
