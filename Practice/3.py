#문자열 뒤집기
s = input()

changing = s.count('10') + s.count('01')

result = (changing + 1) // 2 

print(result)