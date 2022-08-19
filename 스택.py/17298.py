import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
#n=4
#arr=[3,5,2,7]
#ans=[3,-1,-1,-1]
stack = []
stack.append(0)
answer = [-1 for i in range(n)]
#stack=[1,2]
for i in range(1,n):
    while stack and arr[stack[-1]] < arr[i]:
        answer[stack.pop()] = arr[i]
    stack.append(i)
print(*answer)
#i=0 while stack and arr[stack[-1]] <arr[0]  5
# stack=[0]