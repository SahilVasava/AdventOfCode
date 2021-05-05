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


def check_field(pas):
    byr = int(pas.get('byr'))
    iyr = int(pas.get('iyr'))
    eyr = int(pas.get('eyr'))
    hgt = pas.get('hgt')
    hcl = pas.get('hcl')
    ecl = pas.get('ecl')
    pid = pas.get('pid')
    valid = False
    eclSet = {'amb','blu','brn','gry','grn','hzl','oth'}
    if byr >= 1920 and byr <= 2002 and iyr >= 2010 and iyr <= 2020 and eyr >= 2020 and eyr <= 2030 and ((hgt[-2:] == 'in' and int(hgt[:-2]) >= 59 and int(hgt[:-2]) <= 76) or (hgt[-2:] == 'cm' and int(hgt[:-2]) >= 150 and int(hgt[:-2]) <= 193)) and hcl[0] == '#' and len(hcl[1:]) == 6 and hcl[1:].isalnum() and (ecl in eclSet) and len(pid) == 9 and pid.isdigit():
        valid = True
    return valid


req = {'byr','iyr','eyr','hgt','hcl','ecl','pid'}
valid = 0
for passs in content:
    print(f'{passs} {passs.keys() >= req}')
    if passs.keys() >= req and check_field(passs):
        valid += 1

print(valid)
