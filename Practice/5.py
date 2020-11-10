#볼링공 고르기
n, m = map(int, input().split())


w = list(map(int, input().split()))

count = 0

for i in range(n):
    for j in range(n):
        if w[i] == w[j]:
            count += 1

result = ((n ** 2) - count) // 2
                
print(result)
                