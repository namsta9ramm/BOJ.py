from collections import deque
import queue
queue=deque()
ans=0
a,b,c=map(int,input().split())
graph1=[[list(map(int,input().split())) for _ in range(b)] for _ in range(c)]

 

for i in range(c):
    for j in range(b):
        for k in range(a):
            if graph1[i][j][k]==1:
                
                queue.append([i,j,k])

dx=[-1,1,0,0,0,0]
dy=[0,0,-1,1,0,0]
dz=[0,0,0,0,1,-1]
def bfs():
# queue=[1,1,2]
    while queue:
        z1,x1,y1=queue.popleft()
        #z1= 층 , x1 =세로 y1= 가로 
        for i in range(6):
            nz=z1+dz[i]
            nx=x1+dx[i]
            ny=y1+dy[i]
            
            
            if 0<=nx<b and 0<=ny<a and 0<=nz<c and graph1[nz][nx][ny]==0:
                
                graph1[nz][nx][ny]=graph1[z1][x1][y1]+1                
                queue.append([nz,nx,ny])
#[4,2,2] i=0 q=[3,2,2] , [5,2,2] , [4,1,2] , [4,3,2] ,
bfs()

for i in graph1:
    for j in i:
        for k in j:
            if k==0:
                print('-1')
                exit(0)
        ans=max(ans,max(j))

print(ans-1)            
            
