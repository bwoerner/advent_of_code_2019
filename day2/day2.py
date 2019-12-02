puzzle_input = open('day2/input.txt', 'r')
opcode = puzzle_input.read().split(',')
opcode = [int(i) for i in opcode]

#change inital inputs according to challenge
opcode[1] = 12
opcode[2] = 2

for i in range(0, len(opcode), 4):
    a = opcode[i+1]
    b = opcode[i+2]
    c = opcode[i+3]

    if opcode[i] == 1:
        opcode[c] = opcode[a] + opcode[b]
        #i = i + 4
    elif opcode[i] == 2:
        opcode[c] = opcode[a] * opcode[b]
        #i = i + 4
    elif opcode[i] == 99:
        break

print(opcode[0])