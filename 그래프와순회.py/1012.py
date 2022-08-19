#배추밭이 주어진다.
#첫번째 줄에 테스트케이스가 주어지고 
#가로길이, 세로길이, 배추의 개수가 주어진다.
import sys
sys.setrecursionlimit(10**6)

dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global cnt 
    if x<0 or y<0 or x>=a or y>=b:
        return False
    if list1[y][x]==1:
        cnt=cnt+1
        list1[y][x]=0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True

testcase=int(input())
ans_list=[]
for i in range(testcase):
    a,b,c=map(int,input().split())
    list1=[[0 for _ in range(a)] for _ in range(b)]
    for i in range(c):
        i,j=map(int,input().split())
        list1[j][i]=1
    cnt=0
    graph2=[]
    for i in range(a):
        for j in range(b):
            if dfs(i,j)==True:
                graph2.append(cnt)
                cnt=0

    ans_list.append(len(graph2))

for m in ans_list:
    print(m)
