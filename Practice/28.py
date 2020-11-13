def b_search(array, start, end):
    if start > end:
        return None
        
    mid = (start + end ) // 2
    
    if mid == array[mid]:
        return mid
    elif mid < array[mid]:
        return b_search(array, start, mid - 1)
    else:
        return b_search(array, mid + 1, end)
    
n = int(input())
array = list(map(int, input().split()))
index = b_search(array, 0, n - 1)

if index == None:
    print(-1)
else:
    print(index)