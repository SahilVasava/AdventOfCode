import urllib.request
import itertools

url = 'https://adventofcode.com/2020/day/2/input'
headers = {}
headers['Cookie'] = 'session=<token>'

req = urllib.request.Request(url, headers = headers)
content = urllib.request.urlopen(req).read().decode('utf-8')
content = [ str for str in content.rstrip().split('\n')]
correct = 0
for p in content:
    a = p.split(' ')
    limit = a[0].split('-')
    char = a[1].replace(':','')
    passwd = a[2]
    cnt = passwd.count(char)
    if cnt >= int(limit[0]) and cnt <= int(limit[1]):
        correct += 1
print(correct)
