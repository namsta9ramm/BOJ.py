import sys
sys.setrecursionlimit(10**9)
input=sys.stdin.readline

def dfs(start):
    global cnt 
    visited[start]=cnt
    list1[start].sort(reverse=True)

    for i in list1[start]:
        if not visited[i]:
            cnt=cnt+1
            dfs(i)
            
a,b,c=map(int,input().split())
list1=[[] for _ in range(a+1)]
visited=[0]*(a+1)
for i in range(b):
    v,w=map(int,input().split())
    list1[v].append(w)
    list1[w].append(v)

cnt=1
dfs(c)
for i in range(1,a+1):
    print(visited[i])