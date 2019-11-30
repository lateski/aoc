

def readfile(filename):
    
    with open(filename, 'r') as f:
        return f.read()



def calibrate(input):
    round = 0
    sum = 0
    freqs = set()
    freqs = [0]
    dups = False
    a = [int(x) for x in input.split("\n")]
    while not dups:
        #print('round {}'.format(round))
        for l in a:
            sum += l
            if sum in freqs:
                print("Duplicate frequency {}".format(sum))
                dups = True
                break
            freqs.append(sum)
        
        round += 1
    
calibrate(readfile('input.txt'))
