




def add(i,memory):
    num1Ind = memory[i+1]
    num2Ind = memory[i+2]
    resultInd = memory[i+3]
    memory[resultInd] = memory[num1Ind] + memory[num2Ind]
    return i + 4


def multiply(i,memory):
    num1Ind = memory[i+1]
    num2Ind = memory[i+2]
    resultInd = memory[i+3]
    memory[resultInd] = memory[num1Ind] * memory[num2Ind]
    return i + 4

def runProgram(memory, insPtr, noun, verb):

    memory[1] = noun
    memory[2] = verb
    for ind, code in enumerate(memory):
        print(ind, insPtr)
        if ind == insPtr:        
            if code == 1:
                insPtr = add(ind,memory)
            elif code == 2:
                insPtr = multiply(ind,memory)
            elif code == 99:
                break
        else:
            continue

    print(memory)
    output = memory[0]
    if output == 19690720:
        return output
        print(f'Noun: {noun}  Verb: {verb}')
    return 0

def main():

#	for k in range(4):
#		initial_memory = [ int(x) for x in f.read().split(',')]
    shouldBreak = False
    for noun in range(100):
        for verb in range(100):
            f = open('input.txt','r')
            #print(f.read())
            initial_memory = [ int(x) for x in f.read().split(',')]

            initial_insPtr = 0
            op = runProgram(initial_memory, initial_insPtr, noun, verb)
            if op == 19690720:
                print(f'Noun: {noun}  Verb: {verb} Answer: {100*noun+verb}')
                shouldBreak = True
                break
            #print(initial_memory)
            #print(initial_insPtr)
        if shouldBreak:
            break

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
