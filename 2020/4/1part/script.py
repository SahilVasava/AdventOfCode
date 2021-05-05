import urllib.request
import itertools
import math

req = True
content = []
if req:
    url = 'https://adventofcode.com/2020/day/4/input'
    headers = {}
    headers['Cookie'] = 'session=<token>'

    req = urllib.request.Request(url, headers = headers)
    data = urllib.request.urlopen(req).read().decode('utf-8')
    content = [ {p:f for p,f in [q.split(':') for q in x]}  for x in [k.replace('\n',' ').strip().split(' ') for k in [str for str in data.split('\n\n')]] ] 
else:
    with open('input.txt') as f:
        content = [ list(str.rstrip()) for str in f]

req = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
valid = 0
for passs in content:
    print(f'{passs} {passs.keys() >= req}')
    if passs.keys() >= req:
        valid += 1
print(valid)
