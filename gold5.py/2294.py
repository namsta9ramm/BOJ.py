a,b=map(int,input().split())
list1=[]
dp=[10001]*(b+1)
for i in range(a):
    list1.append(int(input()))
dp[0]=0
for m in list1:
    for n in range(m,b+1):
       dp[n]=min(dp[n],dp[n-m]+1) 

if dp[b]==10001:
    print(-1)
else:
    print(dp[b])
    print(dp)