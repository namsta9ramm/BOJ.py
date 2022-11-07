def solution(triangle):
    a=len(triangle)  #a=5
    dp=[[0]*a for _ in range(a+1)]  #i=2, j=0,1
    dp[1][0]=triangle[0][0]
    for i in range(2,a+1):
        for j in range(i):
            if j==0:
                dp[i][j]=dp[i-1][j]+triangle[i-1][0]
            elif j==i-1:
                
                dp[i][j]=dp[i-1][j-1]+triangle[i-1][-1]
            else:
                dp[i][j]=max(dp[i-1][j],dp[i-1][j-1])+triangle[i-1][j]
                
    answer = max(dp[-1])
   
    return answer

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))