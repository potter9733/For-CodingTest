def rotate(a):
    n = len(a)
    m = len(a[0])
    result = [[0]*n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result


def get(board, move):
    a = 0
    while a == 0:
        if len(board[move]) == 0:
            return 0
        else:
            a = board[move].pop()
        
    return a
    
def solution(board, moves):
    stack = []
    answer = 0
    board = rotate(board)
    print(board)
    
    for move in moves:
        doll = get(board, move-1)
        if len(stack) != 0:
            if doll == stack[-1]:
                stack.pop()
                answer += 2
                continue
            
        if doll == 0:
            continue
        else:    
            stack.append(doll)
    
    return answer

# def pop_zero(arr):
#     while (0 in arr):    
#         arr.remove(0)
#         pop_zero(arr)
#     return arr

# def pop(arr):
#     n = len(arr)
#     if n == 1:
#         return arr
#     else:
#         for i in range(n-1):
#             if arr[i] == arr[i+1]:
#                 arr.remove(arr[i])
#                 arr.remove(arr[i])
#                 n -= 2
#     return(arr)