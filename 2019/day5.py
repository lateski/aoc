with open('input.txt', 'r') as f:
    prog = [int(c) for c in f.read().strip('\n').split(',')]

def read(p, mode):
    if not mode:
        #print('mode off: ',p)
        return prog[p]
    elif mode:
        return p
    

def readopc(p):
    p1_mod = 0
    p2_mod = 0
    p3_mod = 0
    opcode = 0
    if p-10000 > 0:
        p3_mod = 1
        p-=10000
    if p-1000 > 0:
        p1_mod = 1
        p -=1000
    if p-100 > 0:
        p2_mod = 1
        p -= 100
    opcode = p
    return [p1_mod, p2_mod, p3_mod, opcode]

#def write(p, mode_pos, )

pc = 0
inp = 5
while prog[pc] != 99: #99 ends the program

    mod2, mod1, mod3, opc = readopc(prog[pc])
    #print('[OPC]=',prog[pc])
    if opc == 1 or opc == 2:
        p1 = prog[pc+1]
        p2 = prog[pc+2]
        p3 = prog[pc+3]
        if opc == 1:
            #print('modifiers {} {}'.format(mod1, mod2))
            prog[p3] = read(p1, mod1)+read(p2, mod2)
        else:
            prog[p3] = read(p1, mod1)*read(p2, mod2)
        pc += 4
    elif opc == 3 or opc == 4:
        if opc == 3:
            p1 = prog[pc+1]
            prog[p1] = inp
            print('storing input {} to pos [{}]'.format(inp, p1))
        elif opc == 4:
            print('at pos {} output: {}'.format(pc, read(prog[pc+1], mod1)))
        pc += 2
    elif opc == 5 or opc == 6:
        p1 = prog[pc+1]
        p2 = prog[pc+2]
        p1 = read(p1, mod1)
        p2 = read(p2, mod2)
        if (opc == 5 and p1) or (opc == 6 and p1 == 0):
            #print('jump to [{}]'.format(p2))
            pc = p2
        else:
            pc += 3
    elif opc in [7,8]:
        p1 = prog[pc+1]
        p2 = prog[pc+2]
        p3 = prog[pc+3]
        if opc == 7:
            if read(p1, mod1) < read(p2, mod2):
                prog[p3] = 1
            else:
                prog[p3] = 0
        elif opc == 8:
            if read(p1, mod1) == read(p2, mod2):
                prog[p3] = 1
            else:
                prog[p3] = 0
        pc+=4
    else:
        print('unknown opc is {}'.format(opc))
        break

#print(prog[0])

