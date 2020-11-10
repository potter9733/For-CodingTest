#모험가 길드
n = int(input())

d_list = list(map(int, input().split()))

d_list.sort()

idx = n - 1
count = 0

while idx >= -1:
    if d_list[idx] - idx <= 1:
        count += 1
    idx = idx - d_list[idx]
    
print(count)