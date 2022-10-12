from collections import deque

n,k=map(int,input().split())

def bfs():
    max=100000
    dict=[-1]*(max+1)
    q=deque([n])
    
    dict[n]=0

    while q:
        x=q.popleft()
        
        if x==k:
            return dict[x]
            
        
        for i in (2*x,x-1,x+1):
            if 0<=i<=100000 and dict[i]==-1:
                    if i==2*x:
                        q.append(i)
                        dict[i]=dict[x]
                    else:
                        q.append(i)
                        dict[i]=dict[x]+1



print(bfs())