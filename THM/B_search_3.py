#떡볶이 떡 만들기
n, hope = map(int, input().split())

d_list = list(map(int, input().split()))
d_list.sort()

start, end = 0, max(d_list)

while start <= end:
    mid = (start + end) // 2
    sum = 0
    for x in d_list:
        if x - mid > 0:
            sum += x - mid
    
    if sum < hope:
        end = mid - 1
        
    else:
        result = mid
        start = mid + 1

print(result)        