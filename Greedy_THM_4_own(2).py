#1이 될 때까지

n, k = map(int, input().split())

count = 0

while n != 1:
    target = (n // k) * k
    count += n - target
    n = target
    target = n // k
    count += 1
    n = target
    
print(count)