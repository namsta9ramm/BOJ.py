#나이트의 이동
from collections import deque
import queue
#수빈이의 위치가 x일 때 x-1,x+1,2x의 위치로 이동한다.

dx=[1,2,1,2,-1,-2,-1,-2]
dy=[2,1,-2,-1,2,1,-2,-1]

def bfs(v,w,q,p):
    
    queue= deque()
    queue.append([v,w])
    s[v][w]=1
    while queue:
        nx,ny = queue.popleft()
        if nx==q and ny==p:
            print(s[q][p]-1)
            return
        for i in range(8):
            x=nx+dx[i]
            y=ny+dy[i]
            
            if 0<=x<a and 0<=y<a and s[x][y]==0:
                queue.append([x,y])
                s[x][y]=s[nx][ny]+1
t=int(input())
for _ in range(t):
    a=int(input())
    v,w=map(int,input().split())
    q,p=map(int,input().split())
    s=[[0]*a for _ in range(a)]
    
    bfs(v,w,q,p)
