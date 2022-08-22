from collections import deque
import queue
queue=deque()
ans=0
a,b=map(int,input().split())
graph1=[]
for _ in range(b):
    graph1.append(list(map(int,input().split())))

for i in range(b):
    for j in range(a):
        if graph1[i][j]==1:
            queue.append([i,j])
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def bfs():
    
    while queue:
        x1,y1=queue.popleft()
        
        for i in range(4):
            nx=x1+dx[i]
            ny=y1+dy[i]
            if 0<=nx<b and 0<=ny<a and graph1[nx][ny]==0:
                
                graph1[nx][ny]=graph1[x1][y1]+1
                queue.append([nx,ny])
bfs()
for i in graph1:
    for j in i:
        if j==0:
            print('-1')
            exit(0)
    ans=max(ans,max(i))

print(ans-1)            
            
    

