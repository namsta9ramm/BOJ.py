from collections import deque

n,k=map(int,input().split())


ans_count=0
ans=0
num=100000
dict=[0]*(num+1)
dict[n]=0
q=deque()
q.append(n)
while q:
        x=q.popleft()
        if x==k:
            ans_count=dict[x]
            ans=ans+1
            continue
        for i in [x-1,x+1,2*x]:
            if 0<=i<=100000: 
                if dict[i]==0 or dict[i]==dict[x]+1:
                    q.append(i)
                    dict[i]=dict[x]+1

print(ans_count)
print(ans)
