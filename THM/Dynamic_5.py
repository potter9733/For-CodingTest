#효율적인 화폐 구성

n, m = map(int, input().split())

coins = []

for _ in range(n):
    coins.append(int(input()))
    
coins.sort()

targets = [10001] * (m + 1)

targets[0] = 0

for i in range(n):
    for j in range(coins[i], m+1):
        if targets[j - coins[i]] != 10001:
            targets[j] = min(targets[j], targets[j - coins[i]] + 1)
            
if targets[m] == 10001:
    print(-1)
else:
    print(targets[m])