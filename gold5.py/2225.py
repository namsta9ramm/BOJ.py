a,b=map(int,input().split())
dp=[[0]*201 for i in range(201)]
for i in range(201):
    dp[i][1]=1

for n in range(1,201):
    for j in range(201):
        for m in range(j+1):

            dp[j][n]=dp[j][n]+dp[m][n-1]

print(dp[a][b]%1000000000)