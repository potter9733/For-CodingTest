#음료수 얼려 먹기
 
n, m = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input())))
    
    
def dfs(x, y):
    if x <= -1 or x >= n or y <= -1 or y >= n:
        return False
    
    if graph[x][y] == 0:
        #해당 노드 방문 처리
        graph[x][y] = 1
        
        #상 하 좌 우 위치를 모두 재귀적 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False
    
result = 0
for i in range(n):
    for j in range(m):
        if dfs(i, j) == True:
            result += 1
            
print(result)
        