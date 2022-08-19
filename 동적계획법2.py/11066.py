import sys
input = sys.stdin.readline
def solve():
    K = int(input())
    arr = [0] + list(map(int, input().split()))
    
    dp = [[0]*(K+1) for _ in range(K+1)]

    # 먼저 dp[i][i+1]을 구한다.두 파일이 연속으로 되어있을 때의 합을 구하는 경우만 dp에 저장한다.
    for i in range(1, K+1):
        for j in range(1, K+1):
            if j==i+1:
                dp[i][j] = arr[i] + arr[j]

    # dp의 맨 밑에서부터 위로 올라오면서 dp를 채워 나간다.
    for i in range(K-1, 0, -1):
        for j in range(1, K+1):
            if dp[i][j] == 0 and j>i:
                dp[i][j] = min([dp[i][k]+dp[k+1][j] for k in range(i,j)]) + sum(arr[i:j+1])
    
    print(dp[1][K])
T = int(input())
for _ in range(T):
    solve()