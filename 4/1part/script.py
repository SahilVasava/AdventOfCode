
def diffBet(n1,n2):
    return n1 - n2


def generatePass(rangeNos):
    passList = []
    for num in range(rangeNos[0], rangeNos[1]+1):
        valid = True
        double = False
        ints = [ int(n) for n in str(num) ]
        for ind, val in enumerate(ints):
            if len(ints) == ind+1:
                break
            if diffBet(ints[ind+1], ints[ind]) < 0:
                valid = False
                break
            elif diffBet(ints[ind+1], ints[ind]) == 0:
                double = True
        if valid and double:
            passList.append(num)
    return passList


def main():
    f = open('input.txt','r')
    rangeNos = [int(x) for x in f.readline().split('-')]
    passList = generatePass(rangeNos)
    print(len(passList))

if __name__ == '__main__':
    main()
