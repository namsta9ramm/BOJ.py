import sys
from itertools import combinations
n=int(input())
answer=[]
for j in range(1,11):
    for i in combinations(range(10),j):
        num=sorted(list(i), reverse=True)
        answer.append(int("".join(map(str,num))))

answer.sort()
print(answer[n] if len(answer)>n else -1)
