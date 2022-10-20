a=int(input())
list1=[]


max_dp=[0]*3 
min_dp=[0]*3
use1_dp=[0]*3
use2_dp=[0]*3

for i in range(a):
    a,b,c=map(int,input().split())
    for j in range(3):
        if j==0:
            max_dp[j]=a+max(use1_dp[j],use1_dp[j+1])
            min_dp[j]=a+min(use2_dp[j],use2_dp[j+1])
            
        elif j==2:
            max_dp[j]=c+max(use1_dp[j],use1_dp[j-1])
            min_dp[j]=c+min(use2_dp[j],use2_dp[j-1])
            
        elif j==1:
            max_dp[j]=b+max(use1_dp[j],use1_dp[j+1],use1_dp[j-1])
            min_dp[j]=b+min(use2_dp[j],use2_dp[j+1],use2_dp[j-1])
    
    for m in range(3):
        use1_dp[m]=max_dp[m]
        use2_dp[m]=min_dp[m]
print(max(use1_dp),min(use2_dp))
