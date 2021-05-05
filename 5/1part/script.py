
import sys



def inputOp(i,pmode,memory):
    inputNum = int(sys.argv[-1])
    resultInd = getIndexM(pmode[-1],i+1,memory)
    memory[resultInd] = inputNum
#    print(f'InputOp:')
    return i + 2


def outputOp(i,pmode,memory):
    resultInd = getIndexM(pmode[-1],i+1,memory)
    print(f'Output: {memory[resultInd]}')
    return i + 2


def add(i,pmode,memory):
    num1Ind = getIndexM(pmode[-1],i+1,memory)
    num2Ind = getIndexM(pmode[-2],i+2,memory)
    resultInd = getIndexM(pmode[-3],i+3,memory)
    memory[resultInd] = memory[num1Ind] + memory[num2Ind]
#    print(f'Add:')
    return i + 4

def getIndexM(pm, index, memory):
    if pm == '0':
        return memory[index]
    elif pm == '1':
        return index


def multiply(i,pmode,memory):
    num1Ind = getIndexM(pmode[-1],i+1,memory)
    num2Ind = getIndexM(pmode[-2],i+2,memory)
    resultInd = getIndexM(pmode[-3],i+3,memory)
    memory[resultInd] = memory[num1Ind] * memory[num2Ind]
#    print(f'Multiply:')
    return i + 4

def runProgram(memory, insPtr, noun, verb):

#    memory[1] = noun
#    memory[2] = verb
    for ind, opcode in enumerate(memory):
#        print(ind, insPtr)
        opcode = str(opcode).zfill(5)
        code = int(opcode[-2:])
        pmode = opcode[:-2]
#        print(f'opcode: {opcode} code: {code} pmode: {pmode}')
        if ind == insPtr:        
            if code == 1:
                insPtr = add(ind,pmode,memory)
            elif code == 2:
                insPtr = multiply(ind,pmode,memory)
            elif code == 3:
                insPtr = inputOp(ind,pmode,memory)
            elif code == 4:
                insPtr = outputOp(ind,pmode,memory)
            elif code == 99:
                break
        else:
            continue

#    print(memory, memory[255])
#    output = memory[0]
#    if output == 19690720:
#        return output
#        print(f'Noun: {noun}  Verb: {verb}')
    return 0

def main():

#	for k in range(4):
#		initial_memory = [ int(x) for x in f.read().split(',')]
#    shouldBreak = False
#    for noun in range(100):
#        for verb in range(100):
            f = open('input.txt','r')
            #print(f.read())
            initial_memory = [ int(x) for x in f.read().split(',')]

            initial_insPtr = 0
#            print(initial_memory, initial_memory[255])
            op = runProgram(initial_memory, initial_insPtr, 0, 0)
#            if op == 19690720:
#                print(f'Noun: {noun}  Verb: {verb} Answer: {100*noun+verb}')
#                shouldBreak = True
#                break
#            #print(initial_memory)
#            #print(initial_insPtr)
#        if shouldBreak:
#            break

if __name__ == '__main__':
    main()



#def operation(i, op):
#    num1Ind = memory[i+1]
#    num2Ind = memory[i+2]
#    resultInd memory[i+3]
#    if op == 'add':
#        memory[resultInd] = memory[num1Ind] + memory[num2Ind]
#    elif op == 'multiply':
#        memory[resultInd] = memory[num1Ind] * memory[num2Ind]
#    return 
