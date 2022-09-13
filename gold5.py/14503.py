import sys
input=sys.stdin.readline
from collections import deque

a,b=map(int,input().split())
x,y,d=map(int,input().split())
list1=[]
for _ in range(a):
    list1.append(list(map(int,(input().split()))))
graph=[[0]*b for _ in range(a)]

#동쪽,서쪽,남쪽,북쪽
dx=[-1,0,1,0]
dy=[0,1,0,-1]
list1[x][y]=1
cnt=1

while True:
    flag=0
    for _ in range(4):
        nx=x+dx[(d+3)%4]
        ny=y+dy[(d+3)%4]
        d=(d+3)%4

        if 0<= nx< a and 0<=ny<b and list1[nx][ny]==0:
            if graph[nx][ny]==0:
                graph[nx][ny]=1
                cnt=cnt+1
                x=nx
                y=ny
                flag=1
                break
    if flag==0:
        if list1[x-dx[d]][y-dy[d]]==1:
            print(cnt)
            break
        else:
            x,y=x-dx[d],y-dy[d]