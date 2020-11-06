#숫자 카드 게임

n, m = map(int, input().split())

for _ in range(n):
    data = list(map(int, input().split()))
    min_temp = min(data)
    min_value = max(0, min_temp)
    
print(min_value)