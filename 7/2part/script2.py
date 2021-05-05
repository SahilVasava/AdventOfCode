
import sys
from itertools import permutations


class computer:

    def __init__(self, memory, ps):
        self.memory = memory
        self.insPtr = 0
        self.ps = ps
        self.inputMode = 'ps'
        self.done = False

    def jmpT(self, pmode):
        num1Ind = self.getIndexM(pmode[-1], self.insPtr+1)
        num2Ind = self.getIndexM(pmode[-2], self.insPtr+2)
        if self.memory[num1Ind] != 0:
            self.insPtr = self.memory[num2Ind]
            return
        self.insPtr += 3

    def jmpF(self, pmode):
        num1Ind = self.getIndexM(pmode[-1], self.insPtr+1)
        num2Ind = self.getIndexM(pmode[-2], self.insPtr+2)
        if self.memory[num1Ind] == 0:
            self.insPtr = self.memory[num2Ind]
            return
        self.insPtr += 3

    def lessThan(self, pmode):
        num1Ind = self.getIndexM(pmode[-1], self.insPtr+1)
        num2Ind = self.getIndexM(pmode[-2], self.insPtr+2)
        resultInd = self.getIndexM(pmode[-3], self.insPtr+3)
        if self.memory[num1Ind] < self.memory[num2Ind]:
            self.memory[resultInd] = 1
        else:
            self.memory[resultInd] = 0
        self.insPtr += 4

    def equalsOp(self, pmode):
        num1Ind = self.getIndexM(pmode[-1], self.insPtr+1)
        num2Ind = self.getIndexM(pmode[-2], self.insPtr+2)
        resultInd = self.getIndexM(pmode[-3], self.insPtr+3)
        if self.memory[num1Ind] == self.memory[num2Ind]:
            self.memory[resultInd] = 1
        else:
            self.memory[resultInd] = 0
        self.insPtr += 4

    def inputOp(self, pmode, ops):
        print(f'ps {self.ps} inputMode {self.inputMode} ops {ops}')
        if self.inputMode == 'ps':
            inputNum = self.ps
        elif self.inputMode == 'input':
            inputNum = ops
        resultInd = self.getIndexM(pmode[-1], self.insPtr+1)
        self.memory[resultInd] = inputNum
    #    print(f'InputOp:')
        self.insPtr += 2

    def outputOp(self, pmode):
        resultInd = self.getIndexM(pmode[-1], self.insPtr+1)
        print(f'Output: {self.memory[resultInd]}')
        self.insPtr += 2
        return self.memory[resultInd]

    def add(self, pmode):
        num1Ind = self.getIndexM(pmode[-1], self.insPtr+1)
        num2Ind = self.getIndexM(pmode[-2], self.insPtr+2)
        resultInd = self.getIndexM(pmode[-3], self.insPtr+3)
        self.memory[resultInd] = self.memory[num1Ind] + self.memory[num2Ind]
    #    print(f'Add:')
        self.insPtr += 4

    def getIndexM(self, pm, index):
        if pm == '0':
            return self.memory[index]
        elif pm == '1':
            return index

    def multiply(self, pmode):
        num1Ind = self.getIndexM(pmode[-1], self.insPtr+1)
        num2Ind = self.getIndexM(pmode[-2], self.insPtr+2)
        resultInd = self.getIndexM(pmode[-3], self.insPtr+3)
        self.memory[resultInd] = self.memory[num1Ind] * self.memory[num2Ind]
    #    print(f'Multiply:')
        self.insPtr += 4

    def runProgram(self, ops):

        #    self.memory[1] = noun
        #    self.memory[2] = verb

        while True:
            #    for ind, opcode in enumerate(self.memory):
            #        print(ind, insPtr)
            opcode = self.memory[self.insPtr]
            opcode = str(opcode).zfill(5)
            code = int(opcode[-2:])
            pmode = opcode[:-2]
    #        print(f'opcode: {opcode} code: {code} pmode: {pmode}')
    #        if ind == insPtr:
            print(f'Inside run {self.insPtr}')
            if code == 1:
                print('Add...')
                self.add(pmode)
            elif code == 2:
                print('multiply...')
                self.multiply(pmode)
            elif code == 3:
                print('inputOp...')
                self.inputOp(pmode, ops)
                self.inputMode = 'input'
            elif code == 4:
                print('outputOp...')
                return self.outputOp(pmode)
            elif code == 5:
                print('jmpT...')
                self.jmpT(pmode)
            elif code == 6:
                print('jmpF...')
                self.jmpF(pmode)
            elif code == 7:
                print('lessThan...')
                self.lessThan(pmode)
            elif code == 8:
                print('equalsOp...')
                self.equalsOp(pmode)
            elif code == 99:
                print('Breaking...')
                self.done = True
                return None
            # else:
            #     continue

    #    print(self.memory, self.memory[255])
    #    output = self.memory[0]
    #    if output == 19690720:
    #        return output
    #        print(f'Noun: {noun}  Verb: {verb}')
    #   return ops


def amplify(prog_str, phaseSeq):
    ops = 0
    for phase in phaseSeq:
        comp = computer(list(map(int, prog_str.split(','))), phase)
        ops = comp.runProgram(ops)
    return ops


def feedback_amplify(prog_str, phaseSeq):
    ops = 0
    last_valid = None
    comps = [
        computer(list(map(int, prog_str.split(','))), phase) for phase in phaseSeq
    ]
    while not any([comp.done for comp in comps]):
        for i in range(5):
            print(f'Runing...{comps[i].memory} {comps[i].insPtr}')
            ops = comps[i].runProgram(ops)
            print(f'Oppppss: {ops}')
            if ops is not None:
                last_valid = ops
        print(any([comp.done for comp in comps]))
    return last_valid


def main():

    # combs = permutations([0, 1, 2, 3, 4])
    # combs = permutations([5,6,7,8,9])

    f = open('input.txt', 'r')
    prog_str = f.read()
    # max_thrust = max([amplify(prog_str, comb) for comb in list(permutations([0, 1, 2, 3, 4]))])
    # print(f'Max Thrust Signal: {max_thrust}')
    max_feedback_thrust = max([feedback_amplify(prog_str, comb)
                               for comb in list(permutations([5, 6, 7, 8, 9]))])
    print(f'Max Thrust Signal: {max_feedback_thrust}')
    # for phaseSeq in list(combs):
    # initial_memory = [ arr for phase in phaseSeq [ int(x) for x in prog_str.split(',')] ]
    # memory = [int(x) for x in prog_str.split(',')]

    # while ops is not None:
    #     for amp in range(5):

    #         ops = runProgram(ops)
    #         thrustSig.append(ops)
    # print(f'Seq: {ps} OPS: {ops}')


if __name__ == '__main__':
    main()


# def operation(i, op):
#    num1Ind = memory[i+1]
#    num2Ind = memory[i+2]
#    resultInd memory[i+3]
#    if op == 'add':
#        memory[resultInd] = memory[num1Ind] + memory[num2Ind]
#    elif op == 'multiply':
#        memory[resultInd] = memory[num1Ind] * memory[num2Ind]
#    return
