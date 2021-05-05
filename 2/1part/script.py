f = open('input.txt','r')

programArr = [ int(x) for x in f.read().split(',')]
#print(programArr)

opcodeInd = 0


#1202 program alarm state
programArr[1] = 12
programArr[2] = 2



def add(i):
    num1Ind = programArr[i+1]
    num2Ind = programArr[i+2]
    resultInd = programArr[i+3]
    programArr[resultInd] = programArr[num1Ind] + programArr[num2Ind]
    return i + 4


def multiply(i):
    num1Ind = programArr[i+1]
    num2Ind = programArr[i+2]
    resultInd = programArr[i+3]
    programArr[resultInd] = programArr[num1Ind] * programArr[num2Ind]
    return i + 4


for ind, code in enumerate(programArr):
    if ind == opcodeInd:        
        if code == 1:
            opcodeInd = add(ind)
        elif code == 2:
            opcodeInd = multiply(ind)
        elif code == 9:
            break
    else:
        continue

print(programArr[0])




#def operation(i, op):
#    num1Ind = programArr[i+1]
#    num2Ind = programArr[i+2]
#    resultInd programArr[i+3]
#    if op == 'add':
#        programArr[resultInd] = programArr[num1Ind] + programArr[num2Ind]
#    elif op == 'multiply':
#        programArr[resultInd] = programArr[num1Ind] * programArr[num2Ind]
#    return 
