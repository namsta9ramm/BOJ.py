#첫줄에 DFS 두번째줄에 BFS
import queue
import sys 
from collections import deque

def bfs(graph,start,visited):
    global order_num
    queue=deque([start])
    visited[start]=True
    while queue:
        v=queue.popleft()
        order[v]=order_num
        order_num+=1
        print(v,end=" ")
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i]=True
def dfs(start):
    global cnt 
    visited_D[start]=cnt
    graph[start].sort()
    print(start,end=" ")
    for i in graph[start]:
        if not visited_D[i]:
            cnt=cnt+1
            dfs(i)


a,b,c=map(int,input().split())
graph=[ [] for _ in range(a+1)]
for _ in range(b):
    u,v=map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)
for g in graph:
    g.sort()

visited=[False]*(a+1)
order=[0]*(a+1)
visited_D=[0]*(a+1)
order_num=1
cnt=1
dfs(c)
print()
bfs(graph,c,visited)




