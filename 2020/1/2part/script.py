import urllib.request
import itertools

headers = {}
headers['Cookie'] = 'session=<token>'
req = urllib.request.Request('https://adventofcode.com/2020/day/1/input', headers = headers)
content = urllib.request.urlopen(req).read().decode('utf-8')
content = [ int(str) for str in content.rstrip().split('\n')]
for a,b,c in itertools.combinations(content,3):
    if a + b + c == 2020:
        print(a*b*c)
