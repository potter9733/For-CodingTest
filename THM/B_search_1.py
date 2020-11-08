#이진탐색 method (반복문)

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


n, t = map(int, input().split())

d_list = list(map(int, input().split()))

result = b_search(d_list, t, 0, n-1)
if result == None:
    print("찾을 수 없음")
else:
    print(f'{result+1}번째에 값 있음!')