#상하좌우

#n = int(input())
#directions = list(map(str,input().split()))

n=5
directions = 'R R R U D D'

route = '11' + directions.replace(' ', '')
route = route.replace('R','0,1')
route = route.replace('L','0,-1')
route = route.replace('U','-1,0')
route = route.replace('D','1,0')
route = route.split(',')

x = 0
y = 0

for i in route[::2]:
    dx = int(i)
    if x + dx < 1 or x + dx > n:
        continue
    x += dx
    
for i in route[1::2]:
    dy = int(i)
    if y + dy < 1 or y + dy > n:
        continue
    y += dy
    
print(x, y)

