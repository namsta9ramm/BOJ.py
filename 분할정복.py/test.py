def solution(dots):
    #testcase1
    answer=0
    if dots[0][1]-dots[1][1]!=0 and dots[2][1]-dots[3][1]!=0:
        a=(dots[0][0]-dots[1][0])/(dots[0][1]-dots[1][1])
        b=(dots[2][0]-dots[3][0])/(dots[2][1]-dots[3][1])
        if a==b:
            answer = answer+1
    if dots[0][1]-dots[1][1]==0 and dots[2][1]-dots[3][1]==0:
        answer = answer+1
    
    
    if dots[0][1]-dots[2][1]!=0 and dots[1][1]-dots[3][1]!=0:
        a1=(dots[0][0]-dots[2][0])/(dots[0][1]-dots[2][1])
        b1=(dots[1][0]-dots[3][0])/(dots[1][1]-dots[3][1])
        if a1==b1:
            answer = answer+1
    if dots[0][1]-dots[2][1]==0 and dots[1][1]-dots[3][1]==0:
        answer = answer+1
    

    if dots[0][1]-dots[3][1]!=0 and dots[1][1]-dots[2][1]!=0:
        a2=(dots[0][0]-dots[3][0])/(dots[0][1]-dots[3][1])
        b2=(dots[1][0]-dots[2][0])/(dots[1][1]-dots[2][1])
        if a2==b2:
            answer = answer+1
    if dots[0][1]-dots[3][1]==0 and dots[1][1]-dots[2][1]==0:
    
    
        answer = answer+1
    
    
    
    
    
    
    if answer==0:
        return 0
    else:
        return 1