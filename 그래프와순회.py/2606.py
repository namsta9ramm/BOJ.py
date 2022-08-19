#바이러스 
#바이러스는 1번 컴퓨터에서 시작된다
#바이러스에 걸리게 되는 컴퓨터의 수 출력
import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(start):
    global cnt 
    visited[start]=cnt
    list1[start].sort()

    for i in list1[start]:
        if not visited[i]:
            cnt=cnt+1
            dfs(i)
            
a=int(input())
b=int(input())
list1=[[] for _ in range(a+1)]
visited=[0]*(a+1)

for i in range(b):
    v,w=map(int,input().split())
    list1[v].append(w)
    list1[w].append(v)

cnt=1
dfs(1)
print(a-visited.count(0))
