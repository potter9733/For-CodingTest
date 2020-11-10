#곱하기 혹은 더하기
s = input()
sum = 0

for n in s:
    if int(n) == 0 or int(n) == 1 or sum == 0 or sum == 1:
        sum += int(n)
    else:
        sum *= int(n)
        
print(sum)