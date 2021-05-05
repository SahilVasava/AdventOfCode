def minSteps(interSet, line1, line2):
    stepList = []
    for p in interSet:
        x = 0
        y = 0
        while len(line1) > 0:
            if p == line1[x]:
                x += 1
                break
            x += 1
        while len(line2) > 0:
            if p == line2[y]:
                y += 1
                break
            y += 1
        stepList.append(x+y)
    print(f'StepList: {stepList} Minsteps: {min(stepList)}')

def manhattanDis(interSet):
    disList = []
    for p in interSet:
        disList.append(abs(p[0]-0)+ abs(p[1]-0))
    return disList

def intersection(line1, line2):
    line1_set = set(line1)
    line2_set = set(line2)
#    if line1_set & line2_set:
#        print(line1_set & line2_set)
    if len(line1_set.intersection(line2_set)) > 0:
        print(line1_set.intersection(line2_set))
        return line1_set.intersection(line2_set)
#    for point in line1:
#        if point in line2:
#            print(point)


def getPoints(wire):
    line = []
    x = 0
    y = 0
    for dir in wire:
        if dir[0] == 'U':
            line.extend([ (x, y+j) for j in range(1,int(dir[1:])+1) ])
            x = line[-1][0]
            y = line[-1][1]
        elif dir[0] == 'D':
            line.extend([ (x, y-j) for j in range(1,int(dir[1:])+1) ])
            x = line[-1][0]
            y = line[-1][1]
        elif dir[0] == 'R':
            line.extend([ (x+i, y) for i in range(1,int(dir[1:])+1) ])
            x = line[-1][0]
            y = line[-1][1]
        elif dir[0] == 'L':
            line.extend([ (x-i, y) for i in range(1,int(dir[1:])+1) ])
            x = line[-1][0]
            y = line[-1][1]
    return line

#def getGraph(wire1, wire2):
#    line1 = []
#    line2 = []


def main():

    f = open('input.txt','r')
    wire1 = f.readline().strip().split(',')
    wire2 = f.readline().strip().split(',')
    line1 = getPoints(wire1)
    line2 = getPoints(wire2)
    interSet = intersection(line1, line2)
    disList = manhattanDis(interSet)
    minSteps(interSet, line1, line2)
    print(min(disList))
#    print(line1[0:1010])

if __name__ == '__main__':
    main()
