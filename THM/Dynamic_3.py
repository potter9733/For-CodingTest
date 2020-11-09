#개미 전사
n = int(input())

a = [0] * (n + 1)

d_list = list(map(int, input().split()))

a[1] = d_list[0]

a[2] = max(d_list[0], d_list[1])

for i in range(3, n + 1):
    a[i] = max( a[i-1], a[i-2] + d_list[i-1])
    
print(a[n])