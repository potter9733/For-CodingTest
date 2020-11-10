#문자열 재정렬
data = input()
array = []
sum = 0
for i in data:
    if i.isalpha():
        array.append(i)
    else:
        sum += int(i)
        
array.sort()

array.append(str(sum))

print(''.join(array))

