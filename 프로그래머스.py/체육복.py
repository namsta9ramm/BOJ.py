
def solution(n, lost, reserve):
    #reserve=[1, 2, 5, 6, 10, 12, 13]
    #lost=[2, 3, 4, 5, 7, 8, 9, 10, 11, 12]
    set1=set(lost)
    set2=set(reserve)
    lost=list(set1-(set1&set2))
    reserve=list(set2-(set1&set2))
    
    for i in reserve:
        if i-1 in lost:
            lost.remove(i-1)
      
        elif i+1 in lost:
            lost.remove(i+1)
        print(lost)

        
    return n-len(lost)
print(solution(13, [1, 2, 5, 6, 10, 12, 13], [2, 3, 4, 5, 7, 8, 9, 10, 11, 12]))
