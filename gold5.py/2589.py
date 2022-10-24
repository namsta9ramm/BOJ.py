from collections import deque
dx=[1,-1,0,0]
dy=[0,0,1,-1]
def bfs(i,j):
    q=deque()
    q.append([i,j])
    max_num=0
    while q:
        a,b=q.popleft()

        for i in range(4):
            x=a+dx[i]
            y=b+dy[i]
            if 0<=x<=n and 0<=y<=m and visit[x][y]==0 and list1[x][y]!="W":
                list1[x][y]=list1[a][b]+1
                visit[x][y]=1
                q.append([x,y])
                max_num=max(max_num,list1[x][y])
    return max_num
n,m=map(int,input().split())
list1=[]
for _ in range(n):
    list1.append(list(input().strip()))
list2=[[0]*m for _ in range(n)]
ans=0
for i in range(n):
    for j in range(m):
        if list1[i][j]!="W":
            list1[i][j]=0
            visit=[[0]*m for _ in range(n)]
            ans=max(ans,bfs(i,j))