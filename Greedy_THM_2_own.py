#큰 수의 법칙

n, m, k = map(int, input().split())

data = list(map(int, input().split()))

data.sort()

first = data[-1]
second = data[-2]

result = ( first * k + second ) * (m // (k+1)) + first * (m % (k+1))

print(result)