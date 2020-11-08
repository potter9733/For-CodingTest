#부품 찾기
def b_search(data, target, start, end):
    
    while start <= end:
        mid = (start + end) // 2
        if data[mid] == target:
            return mid
        elif data[mid] > target:
            end = mid - 1
        else:
            start = mid +1
    return None

n = int(input())

d_list = list(map(int, input().split()))
d_list.sort()

k = int(input())

target = list(map(int, input().split()))

for i in target:
    result = b_search(d_list, i, 0, n-1)
    if result == None:
        print('no', end=' ')
    else:
        print('yes', end=' ')