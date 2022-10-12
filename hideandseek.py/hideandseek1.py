from collections import deque
n,k=map(int,input().split())

def bfs():
    q=deque()
    q.append(n)
    while q:
        x=q.popleft()
        if x==k:
            print(dict[x])
            break
        for i in (x-1,x+1,2*x):
            if 0<=i<=100000 and not dict[i]:
                q.append(i)
                dict[i]=dict[x]+1

dict=[0]*100001

bfs()