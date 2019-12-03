with open('input.txt') as f:
    data = [int(i) for i in f.read().split(',')]



def process(data):
    pc = 0 
    addr1 = 1
    addr2 = 2
    store = 3
    while data[pc] != 99:
        
        val1 = data[data[addr1]]
        val2 = data[data[addr2]]
        op = data[pc]
        if (op == 1):
            res = val1 + val2
        elif (op == 2):
            res = val1*val2
        data[data[store]] = res
        print(val1, val2)
        pc += 4
        addr1 += 4
        addr2 += 4
        store += 4
    return data

def process2(data):
    orig = data.copy()
    for i in range(0,100):
        for j in range(0,100):
            data[1] = i
            data[2] = j
            pc = 0 
            addr1 = 1
            addr2 = 2
            store = 3
            while data[pc] != 99:
                
                val1 = data[data[addr1]]
                val2 = data[data[addr2]]
                op = data[pc]
                if (op == 1):
                    res = val1 + val2
                elif (op == 2):
                    res = val1*val2
                data[data[store]] = res
                #print(val1, val2)
                pc += 4
                addr1 += 4
                addr2 += 4
                store += 4
            if (data[0] == 19690720):
                print("{}".format(i*100+j))
                return (i, j)
            else:
                data=orig.copy()

print(process2(data))