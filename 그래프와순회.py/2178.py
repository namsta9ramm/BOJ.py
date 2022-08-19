#N개의 줄에는 M개의 정수로 미로가 주어진다.
from collections import deque
import queue

def bfs(x,y):   
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    queue=deque()
    queue.append((x,y))
    
    while queue:
        x,y=queue.popleft()
        
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]

            if (0<=nx<a) and (0<=ny<b):
                if graph[nx][ny]==1:
                    graph[nx][ny]=graph[x][y]+1
                    queue.append((nx,ny))
    return graph[a-1][b-1]

a,b=map(int,input().split())
graph=[]
for _ in range(a):
    graph.append(list(map(int,input())))
print(bfs(0,0))

