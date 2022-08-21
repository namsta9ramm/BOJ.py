#수빈이의 위치가 x일 때 x-1,x+1,2x의 위치로 이동한다.
import sys
from collections import deque
input = sys.stdin.readline()
#n=5,k=11
def bfs():
    q = deque()
    q.append(n)
    while q:
        x = q.popleft()
        if x == k:
            print(dist[x])
            break

        for j in (x-1,x+1,x*2): # x=5 j=4,6,10
            if 0<= j <= MAX and not dist[j]:
                dist[j] = dist[x] +1
                q.append(j)
MAX = 100000
n,k = map(int,input.split())
dist = [0] * (MAX+1)
bfs()

