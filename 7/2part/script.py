
import sys
from itertools import permutations


class computer:

    def __init__(self, memory):
        self.memory = memory
        self.insPtr = 0

    def jmpT(self,i, pmode):
        num1Ind = getIndexM(pmode[-1],i+1,self.memory)
        num2Ind = getIndexM(pmode[-2],i+2,self.memory)
        if self.memory[num1Ind] != 0:
            return self.memory[num2Ind]
        return i+3


    def jmpF(self, i, pmode):
        num1Ind = getIndexM(pmode[-1],i+1,self.memory)
        num2Ind = getIndexM(pmode[-2],i+2,self.memory)
        if self.memory[num1Ind] == 0:
            return self.memory[num2Ind]
        return i+3


    def lessThan(self, i, pmode):
        num1Ind = getIndexM(pmode[-1],i+1,self.memory)
        num2Ind = getIndexM(pmode[-2],i+2,self.memory)
        resultInd = getIndexM(pmode[-3],i+3,self.memory)
        if self.memory[num1Ind] < self.memory[num2Ind]:
            self.memory[resultInd] = 1
        else:
            self.memory[resultInd] = 0
        return i + 4

    def equalsOp(self, i, pmode):
        num1Ind = getIndexM(pmode[-1],i+1,self.memory)
        num2Ind = getIndexM(pmode[-2],i+2,self.memory)
        resultInd = getIndexM(pmode[-3],i+3,self.memory)
        if self.memory[num1Ind] == self.memory[num2Ind]:
            self.memory[resultInd] = 1
        else:
            self.memory[resultInd] = 0
        return i + 4


    def inputOp(self, i,pmode,memory,ps,inputMode,amp,ops):
        print(f'ps {ps} inputMode {inputMode} amp {amp} ops {ops}') 
        if inputMode == 'ps':
            inputNum = ps[amp]
        elif inputMode == 'input':
            inputNum = ops
        resultInd = getIndexM(pmode[-1],i+1,self.memory)
        self.memory[resultInd] = inputNum
    #    print(f'InputOp:')
        return i + 2


    def outputOp(self, i,pmode,memory):
        resultInd = getIndexM(pmode[-1],i+1,self.memory)
        print(f'Output: {self.memory[resultInd]}')
        return (i + 2, self.memory[resultInd])


    def add(self, i,pmode,memory):
        num1Ind = getIndexM(pmode[-1],i+1,self.memory)
        num2Ind = getIndexM(pmode[-2],i+2,self.memory)
        resultInd = getIndexM(pmode[-3],i+3,self.memory)
        self.memory[resultInd] = self.memory[num1Ind] + self.memory[num2Ind]
    #    print(f'Add:')
        return i + 4

    def getIndexM(self, pm, index, memory):
        if pm == '0':
            return self.memory[index]
        elif pm == '1':
            return index


    def multiply(self, i,pmode,memory):
        num1Ind = getIndexM(pmode[-1],i+1,self.memory)
        num2Ind = getIndexM(pmode[-2],i+2,self.memory)
        resultInd = getIndexM(pmode[-3],i+3,self.memory)
        self.memory[resultInd] = self.memory[num1Ind] * self.memory[num2Ind]
    #    print(f'Multiply:')
        return i + 4




    def runProgram(self, memory, insPtr, ps, amp, ops):

    #    self.memory[1] = noun
    #    self.memory[2] = verb
        inputMode = 'ps'
        for ind, opcode in enumerate(self.memory):
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
                    print('Breaking...')
                    break
            else:
                continue

    #    print(self.memory, self.memory[255])
    #    output = self.memory[0]
    #    if output == 19690720:
    #        return output
    #        print(f'Noun: {noun}  Verb: {verb}')
        return ops

def main():

    phaseSeq = permutations([5,6,7,8,9])
    thrustSig = []
    f = open('inputtest.txt','r')
    prog_str = f.read()
    for ps in list(phaseSeq):
        ops = 0
        initial_memory = [ arr for phase in phaseSeq [ int(x) for x in prog_str.split(',')] ]
        initial_insPtr = 0
        while ops is not None:
            for amp in range(5):

                ops = runProgram(initial_memory[amp], initial_insPtr, ps, amp, ops)
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
