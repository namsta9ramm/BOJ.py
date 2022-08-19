#정사각형 모양의 지도가 있다.
#단지에 속하는 집의 수를 오름차순으로 정렬후 출력
#N개의 집, 그 안에 속하는 집의 개수 차레대로 출력
#bfs 풀이
from collections import deque
import queue

def bfs(x,y):
    dx=[0,0,1,-1]
    dy=[1,-1,0,0]
    queue=deque()
    queue.append((x,y))
    graph[x][y]=0
    cnt=0
    while queue:
        now=queue.popleft()
        cnt=cnt+1
        for i in range(4):
            nx=now[0]+dx[i]
            ny=now[1]+dy[i]

            if (0<=nx< a) and 0<=ny<a:
                if graph[nx][ny]==1:
                    graph[nx][ny]=0
                    queue.append((nx,ny))
    return cnt

a=int(input())
graph=[]
for _ in range(a):
    graph.append(list(map(int,input())))
result=[]
total=0
for i in range(a):
    for j in range(a):
        if graph[i][j]==1:
            result.append(bfs(i,j))
            total=total+1
result.sort()
print(total)
for i in range(total):
    print(result[i])

