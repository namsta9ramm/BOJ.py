a=int(input())
list1=list(map(int,input().split()))
stack=[]
answer=[0 for _ in range(a)]

for i in range(a):
    while stack:
        if list1[stack[-1]-1]>=list1[i]:
            answer[i]=stack[-1]
            break
        else:
            stack.pop()
    stack.append(i+1)

print(*answer)