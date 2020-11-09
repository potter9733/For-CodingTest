#다이나믹 프로그래밍 (ex. 피보나치 수열)

#Top-Down 방식
d = [None] * 100

def fibo(x):
    
    if x == 1 or x == 2:
        return 1
    
    if d[x] is not None:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))

#Bottom-Up 방식 (권장)
d = [None] * 100
d[1] = 1
d[2] = 1

n = 99

for i in range(3, n+1):
    d[i] = d[i - 1]+d[i - 2]
    
print(d[n])