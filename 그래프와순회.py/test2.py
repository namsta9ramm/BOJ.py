# deque 라이브러리 불러오기
from collections import deque
# BFS 메서드 정의
def bfs (graph, node, visited):
    # 큐 구현을 위한 deque 라이브러리 활용
    queue = deque([node])
    # 현재 노드를 방문 처리
    visited[node] = 1
    
    # 큐가 완전히 빌 때까지 반복
    while queue:
        # 큐에 삽입된 순서대로 노드 하나 꺼내기
        v = queue.popleft()
        graph[v].sort()
        # 탐색 순서 출력
        
        visited[v]=v
        
        # 현재 처리 중인 노드에서 방문하지 않은 인접 노드를 모두 큐에 삽입
        for i in graph[v]:
            if not (visited[i]):
                
                queue.append(i)
                visited[i] =1

list2=[]
a,b,c=map(int,input().split())  
list1=[0]*a
graph=[[] for _ in range(a+1)]
visited = [0] * (a+1)

for i in range(b):
    v,w=map(int,input().split())
    graph[v].append(w)
    graph[w].append(v)

bfs(graph, 1, visited)
