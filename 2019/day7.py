from itertools import permutations
import time

with open('7.in', 'r') as f:
    prog_o = [int(c) for c in f.read().strip('\n').split(',')]

def read(p, mode, prog):
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
def intcode_machine(prog, machine):
    #print('started with input {}'.format(inputstack))
    pc = 0
    output = []
    while prog[pc] != 99: #99 ends the program

        mod2, mod1, mod3, opc = readopc(prog[pc])
        #print('[OPC]=',prog[pc])
        if opc == 1 or opc == 2:
            p1 = prog[pc+1]
            p2 = prog[pc+2]
            p3 = prog[pc+3]
            if opc == 1:
                #print('modifiers {} {}'.format(mod1, mod2))
                prog[p3] = read(p1, mod1, prog)+read(p2, mod2, prog)
            else:
                #print(pc)
                prog[p3] = read(p1, mod1, prog)*read(p2, mod2, prog)
            pc += 4
        elif opc == 3 or opc == 4:
            if opc == 3:
                p1 = prog[pc+1]
                print('[{}] waiting input'.format(machine))
                prog[p1] = yield
                #print('[{}] Got input {}'.format(machine,prog[p1]))
                assert prog[p1] is not None
                #print('[{}] storing input {} to pos [{}]'.format(machine,prog[p1], p1))
            elif opc == 4:
                output.append(read(prog[pc+1], mod1, prog))
                outp = output.pop()
                #print('[{}] yielding {}'.format(machine,outp))
                yield outp
                #print('at pos {} output: {}'.format(pc, read(prog[pc+1], mod1, prog)))
            pc += 2
        elif opc == 5 or opc == 6:
            p1 = prog[pc+1]
            p2 = prog[pc+2]
            p1 = read(p1, mod1, prog)
            p2 = read(p2, mod2, prog)
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
                if read(p1, mod1, prog) < read(p2, mod2, prog):
                    prog[p3] = 1
                else:
                    prog[p3] = 0
            elif opc == 8:
                if read(p1, mod1, prog) == read(p2, mod2, prog):
                    prog[p3] = 1
                else:
                    prog[p3] = 0
            pc+=4
        else:
            print('unknown opc is {}'.format(opc))
            break
    print('Amp with inputs')
    
    return


inp = 0
outputs = []

for p in permutations(range(5,10)):
    
    machines = []
    for i, amp in enumerate(p):
        #inputs[i].append(amp)
        machines.append(intcode_machine(prog_o.copy(), i+1))
        next(machines[i])
        print('sending to machine number {} value {}'.format(i+1, amp))
        machines[i].send(amp)
    inp = 0
    brrr = False
    first = True
    print('-------------------')
    count = 0
    final_output = 0
    while not brrr:
        for vm in machines:
            try:
                if count != 0:
                    next(vm)
                print('vm.send({})'.format(inp))
                inp = vm.send(inp)
                

                final_output = inp
                #print('output {}'.format(inp))
            except StopIteration:
                print('iteration stopped with final output {}'.format(final_output))
                brrr = True
                break
        count += 1
    #time.sleep(1)
    outputs.append(final_output)
    
    
print('max was {}'.format(max(outputs)))
    #print(intcode_machine(prog, [0,4]))
#print(prog[0])

#print(outputs)
#print(max(outputs))