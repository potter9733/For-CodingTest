#성적이 낮은 순서로 학생 출력
n = int(input())

array = []

for _ in range(n):
    data = input().split()
    array.append((data[0], int(data[1])))
    
#i 에서 i[1]값을 return해주는 lambda함수    
array = sorted(array, key = lambda i: i[1])

for i in array:
    print(i[0], end=' ')