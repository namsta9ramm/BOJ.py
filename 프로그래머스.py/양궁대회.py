from itertools import combinations_with_replacement as cwr
from collections import Counter

def solution(n, info):
    answer = []
    info=info[::-1]
    max_n=-1
    k=len(info)
    
    for c in cwr(range(0,k),n):
        ryan=0
        apeach=0
        temp_ans=[0 for _ in range(k)]
        c=Counter(c)
        for i in range(k):
            if info[i]<c[i]:
                ryan=ryan+i
            elif info[i]!=0:
                apeach+=i
            temp_ans[i]=c[i]
        if ryan>apeach:
            diff=ryan-apeach
            if max_n<diff:    
                max_n=diff
                answer=temp_ans
    if answer:
        return answer[::-1]
    else:
        return [max_n]