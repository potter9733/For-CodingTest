#럭키 스트레이트
s = list(input())

n = len(s) // 2

a = s[:n:1]
b = s[:n-1:-1]


sum_a = 0
sum_b = 0

for i in a:
   sum_a += int(i)
   
   
for i in b:
    sum_b += int(i)
    
if sum_a == sum_b:
    print('LUCKY')
    
else:
    print('READY')

