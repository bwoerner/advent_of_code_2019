puzzle_input = open('day2/input.txt', 'r')
opcode = puzzle_input.read().split(',')
opcode = [int(i) for i in opcode]


def get_code(code_list, noun, verb):

    code_list[1] = noun
    code_list[2] = verb

    for i in range(0, len(code_list), 4):
        a = code_list[i+1]
        b = code_list[i+2]
        c = code_list[i+3]
        cmd = code_list[i]

        if cmd == 1:
            code_list[c] = code_list[a] + code_list[b]
        elif cmd == 2:
            code_list[c] = code_list[a] * code_list[b]
        elif cmd == 99:
            break
    return code_list[0]


noun_list = [i for i in range(0,100)]
verb_list = [i for i in range(0,100)]

for noun in noun_list:
    for verb in verb_list:
        current_test = [i for i in opcode] #i cheated on this part because i didn't know how to not lose the inital list
        get_code(current_test, noun, verb)
        if current_test[0] == 19690720:
            print(current_test[0], noun, verb, 100 * noun + verb)
            