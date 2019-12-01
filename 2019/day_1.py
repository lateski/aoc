

with open('input.txt') as f:
    data = [int(i) for i in f.read().splitlines()]

def part1(data):
    totalfuel = 0
    for module in data:
        totalfuel += module//3-2
    return totalfuel

def part2(data):
    totalfuel = 0
    fuel = lambda f: f//3-2
    t_fuel = 0
    for module in data:
        t = module
        while 1:
            t_fuel = fuel(t)
            if t_fuel <= 0:
                break
            else: 
                totalfuel += t_fuel
                t = t_fuel
    return totalfuel
        
    

print(part1(data))
print(part2(data))