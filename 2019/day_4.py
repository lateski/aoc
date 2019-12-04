
def check(l):
    for d in range(len(l)-2):
        if d == 0 and l[d] == l[d+1] != l[d+2]:
            return True
        elif d == len(l)-3 and l[d+1] == l[d+2] != l[d]:
            print(l[d],l[d+1], l[d+2])
            return True            
        elif l[d-1] != l[d] == l[d+1] != l[d+2]:
            print(l[d],l[d+1], l[d+2])
            return True
        print(d-1)
        
    return False
        

c = 0
#for i in range(359282,820401+1):
#    digits = [int(x) for x in str(i)]
#    if digits == sorted(digits):
#        if check(digits):
#            c += 1
#print(c)

check([2,1,1,2])