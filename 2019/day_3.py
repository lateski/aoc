with open('input.txt') as f:
    lines = f.read().splitlines()
    a = lines[0].split(',')
    b = lines[1].split(',')

def get_coords(commands):
    x = y = 0
    line = {}
    lenght = 1
    for ins in commands:
        dx = dy = 0
        c = ins[0]
        di = int(ins[1:])
        if c == 'U':
            dy = 1
        elif c == 'D':
            dy = -1
        elif c == 'R':
            dx = 1
        elif c == 'L':
            dx = -1
        for i in range(di):
            x += dx
            y += dy
            line[(x,y)] = lenght
            lenght +=1   
    return line


union = set(get_coords(a).keys())&set(get_coords(b).keys())
#print(union)
print(min([abs(x)+abs(y) for x,y in union]))

ac = get_coords(a)
bc = get_coords(b)

cur_min = -1

for val in union:
    dis_a = ac[val]
    dis_b = bc[val]
    combined_dis = dis_a + dis_b
    if cur_min == -1:
        cur_min = combined_dis
    elif cur_min > combined_dis:
        cur_min = combined_dis

print(cur_min)
    