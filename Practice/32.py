n = 5
arr = [[0, 0, 0, 0, 0, 0], 
       [0, 7, 0, 0, 0, 0], 
       [0, 3, 8, 0, 0, 0],
       [0, 8, 1, 0, 0, 0], 
       [0, 2, 7, 4, 4, 0], 
       [0, 4, 5, 2, 6, 5]]

max_list = []
for i in range(n-1, 0, -1):
    for j in range(1, n):
        arr[i][j] += max( arr[i+1][j], arr[i+1][j+1] )
    max_list.append(max(arr[i]))
print(max(max_list))
