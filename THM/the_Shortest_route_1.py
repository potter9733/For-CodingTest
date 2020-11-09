#Dijkstra Algorithm using heap

import heapq
#import sys
#input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수
n, m = map(int, input().split())
#시작 노드 번호 입력
start = int(input())
#각 노드에 연결되어 있는 노드에 대한 정보
graph = [ [] for i in range(n+1) ]
#방문여부
visited = [False] * (n + 1)

distance = [INF] * (n + 1)

#모든 간선 정보 입력
for _ in range(m):
    #a노드에서 b로 가는 거리가 c
    a, b, c = map(int, input().split())
    graph[a]. append((b, c))
    
def dijkstra(start):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))
                
dijkstra(start)

for i in range(1, n+1):
    if distance[i] == INF:
        print('INFINITY')
        
    else:
        print(distance[i])