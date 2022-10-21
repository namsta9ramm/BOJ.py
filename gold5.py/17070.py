import sys
input= sys.stdin.readline

N=int(input().strip())
arr = [[1]*(N+2)] + [[1] + list(map(int, input().split())) + [1]
                     for _ in range(N)] + [[1]*(N+2)]
dp = [[[0, 0, 0] for _ in range(N+2)] for __ in range(N+2)]
                     