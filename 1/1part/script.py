import math
f = open('input.txt','r')
#print(f.read())


totalMass = 0
for lines in f:
    totalMass += math.floor(int(lines)/3)-2
print(totalMass)
