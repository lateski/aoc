r = {} #relations
for line in open('6.in').readlines():
    line = line.strip('\n')
    a, orbiter = line.split(')')
    #print(a,orbiter)
    if a in r:
        r[a].append(orbiter)
    else:
        r[a] = [orbiter]

#basically depth counts number of branches in each node
def orbits(planet, dest):
    ans = 0
    has_dest = False
    stats = []
    #print('at planet {}'.format(planet))
    #print('lets see how many planets {} has on its orbit'.format(planet))
    for orbit in r.get(planet, []):
        if orbit == dest:
            has_dest = True
        if not has_dest:
            stats = orbits(orbit, dest)
        
        has_dest = has_dest or stats[1]
        
        if has_dest:
            ans += 1
            break
        #elif (has_you and has_san): 
    if not stats:
        pass
    else:
        ans += stats[0]
        
    return [ans, has_dest]
        

ans = []
routes = {}

for planet in r:
    #print('figuring {}'.format(planet))
    y = orbits(planet, 'YOU')
    s = orbits(planet, 'SAN')
    if s[1] and y[1]:
        #print('Route throug mid node {} would be {} steps'.format(planet,y[0]+s[0]))
        routes[planet] = y[0] + s[0]
    #print(orbits(planet, 'YOU')[0])
    #print(orbits(planet, 'SAN')[0])

print(min([routes[k]-2 for k in routes]))

##Figure out common node