#인접행렬방식
INF = 9999999

graph = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
    ]

print(graph)

#행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)]

#노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7))
graph[0].append((2,5))

#노드 1에 연결된 노드 정보 저장
graph[1].append((0,7))

#노드 2에 연결된 노드 정보 저장
graph[2].append((0,5))

print(graph)

#DFS method
def dfs(graph, v, visited):
    visited[v] = True
    print(v, end=' ')
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
            
graph = [ [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7] ]

visited = [False] * 9

dfs(graph, 1, visited)

#BFS method

from collections import deque

def bfs(graph, start, visited):
    queue = deque([start])
    visited[start] = True
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True
                
graph = [ [], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7] ]

visited = [False] * 9

bfs(graph, 1, visited)
