#너비 우선 탐색 (BFS)
#N개의 정점과 M개의 간선으로 이루어진 무방향 그래프
#정점 번호는 1번부터 N번, 모든 가중치는 1이며 , 인접 정점 오름차순
import queue
import sys 
from collections import deque
input=sys.stdin.readline

def bfs(graph,start,visited):
    global order_num
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        order[v]=order_num
        order_num+=1
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True

a,b,c=map(int,input().split())
graph=[ [] for _ in range(a+1)]
for _ in range(b):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort(reverse=True)

visited=[False]*(a+1)
order=[0]*(a+1)
order_num=1
bfs(graph,c,visited)
for i in range(1,len(order)):
    print(order[i])
