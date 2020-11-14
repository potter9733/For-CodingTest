n, m = 3, 4
arr = [1,3,3,2,2,1,4,1,0,6,4,7]

board = []
for i in range(n):
    board.append(arr[(i*m):(i*m)+m])
board.insert(0,[0]*m)
board.append([0]*m)
max_list = []

for i in range(1, m):
    for j in range(1, n+1):
        board[j][i] += max(board[j-1][i-1], board[j][i-1], board[j+1][i-1])
    max_list.append(max(board[i]))
    
print(max(max_list))