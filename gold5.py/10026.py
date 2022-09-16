from collections import deque

dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(x,y):
    q.append([x,y])
    list2[x][y]=cnt
    
    while q:
        a,b=q.popleft()
        for i in range(4):
            nx=a+dx[i]
            ny=b+dy[i]
            if 0<=nx<num and 0<=ny<num:
                if list1[nx][ny]==list1[x][y] and list2[nx][ny]==0:
                    list2[nx][ny]=1
                    q.append([nx,ny])

num=int(input())
list1=[list(map(str,input())) for _ in range(num)]
list2=[[0]*num for _ in range(num)]
q=deque()
cnt=0
for i in range(num):
    for j in range(num):
        if list2[i][j]==0:
            bfs(i,j)
            cnt=cnt+1
print(cnt,end=" ")

for i in range(num):
    for j in range(num):
        if list1[i][j]=='R':
            list1[i][j]='G'
list2=[[0]*num for _ in range(num)]
cnt=0
for i in range(num):
    for j in range(num):
        if list2[i][j]==0:
            bfs(i,j)
            cnt=cnt+1
print(cnt)