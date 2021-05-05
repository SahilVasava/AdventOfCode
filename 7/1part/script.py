
import sys
from itertools import permutations

def jmpT(i, pmode, memory):
    num1Ind = getIndexM(pmode[-1],i+1,memory)
    num2Ind = getIndexM(pmode[-2],i+2,memory)
    if memory[num1Ind] != 0:
        return memory[num2Ind]
    return i+3


def jmpF(i, pmode, memory):
    num1Ind = getIndexM(pmode[-1],i+1,memory)
    num2Ind = getIndexM(pmode[-2],i+2,memory)
    if memory[num1Ind] == 0:
        return memory[num2Ind]
    return i+3


def lessThan(i, pmode,memory):
    num1Ind = getIndexM(pmode[-1],i+1,memory)
    num2Ind = getIndexM(pmode[-2],i+2,memory)
    resultInd = getIndexM(pmode[-3],i+3,memory)
    if memory[num1Ind] < memory[num2Ind]:
        memory[resultInd] = 1
    else:
        memory[resultInd] = 0
    return i + 4

def equalsOp(i, pmode,memory):
    num1Ind = getIndexM(pmode[-1],i+1,memory)
    num2Ind = getIndexM(pmode[-2],i+2,memory)
    resultInd = getIndexM(pmode[-3],i+3,memory)
    if memory[num1Ind] == memory[num2Ind]:
        memory[resultInd] = 1
    else:
        memory[resultInd] = 0
    return i + 4


def inputOp(i,pmode,memory,ps,inputMode,amp,ops):
    print(f'ps {ps} inputMode {inputMode} amp {amp} ops {ops}') 
    if inputMode == 'ps':
        inputNum = ps[amp]
    elif inputMode == 'input':
        inputNum = ops
    resultInd = getIndexM(pmode[-1],i+1,memory)
    memory[resultInd] = inputNum
#    print(f'InputOp:')
    return i + 2


def outputOp(i,pmode,memory):
    resultInd = getIndexM(pmode[-1],i+1,memory)
    print(f'Output: {memory[resultInd]}')
    return (i + 2, memory[resultInd])


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

#def phaseSettingSeq():



def runProgram(memory, insPtr, ps, amp, ops):

#    memory[1] = noun
#    memory[2] = verb
    inputMode = 'ps'
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
                insPtr = inputOp(ind,pmode,memory,ps,inputMode,amp,ops)
                inputMode = 'input'
            elif code == 4:
                opRes  = outputOp(ind,pmode,memory)
                insPtr = opRes[0]
                ops = opRes[1]
            elif code == 5:
                insPtr = jmpT(ind,pmode,memory)
            elif code == 6:
                insPtr = jmpF(ind,pmode,memory)
            elif code == 7:
                insPtr = lessThan(ind,pmode,memory)
            elif code == 8:
                insPtr = equalsOp(ind,pmode,memory)
            elif code == 99:
                break
        else:
            continue

#    print(memory, memory[255])
#    output = memory[0]
#    if output == 19690720:
#        return output
#        print(f'Noun: {noun}  Verb: {verb}')
    return ops

def main():

    phaseSeq = permutations([0,1,2,3,4])
    thrustSig = []
    for ps in list(phaseSeq):
        ops = 0
        for amp in range(5):

            f = open('input.txt','r')
            initial_memory = [ int(x) for x in f.read().split(',')]
            initial_insPtr = 0
            ops = runProgram(initial_memory, initial_insPtr, ps, amp, ops)
            thrustSig.append(ops)
        print(f'Seq: {ps} OPS: {ops}')
    print(f'Max Thrust Signal: {max(thrustSig)}')
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
