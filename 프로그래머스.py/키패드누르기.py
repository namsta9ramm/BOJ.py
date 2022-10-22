#numvers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
#hand="right"
def solution(numbers, hand):
    answer = ''
    new_list=[[1,2,3],[4,5,6],[7,8,9],['*',0,'#']]
    a1=3
    b1=0
    a2=3 
    b2=2
    a3=0
    b3=0
    for i in numbers:
        
        if i==1 or i==4 or i==7:
            answer+='L'
            for k in new_list:
                if i in k:
                    a1,b1=new_list.index(k),k.index(i) # l(0,0) a1 b1 , r(0,2) a2 b2 , l(1,0) a1 b1 
        elif i==3 or i==6 or i==9:
            answer+='R'
            for k in new_list:                      #r(0,2) l(1,0)
                if i in k:
                    a2,b2=new_list.index(k),k.index(i)
        elif i==2 or i==5 or i==8 or i==0:
            for k in new_list:
                if i in k:
                    a3,b3=new_list.index(k),k.index(i) #(1,1)
                    print(a3,b3,a1,b1,a2,b2)
            if abs(a3-a1)+abs(b3-b1)>abs(a3-a2)+abs(b3-b2):
                    
                    answer+='R'
                    a2=a3
                    b2=b3
            elif abs(a3-a1)+abs(b3-b1)<abs(a3-a2)+abs(b3-b2):
                    answer+='L'
                    a1=a3
                    b1=b3
            elif abs(a3-a1)+abs(b3-b1)==abs(a3-a2)+abs(b3-b2):
                    if hand=="right":
                        answer+='R'
                        a2=a3
                        b2=b3
                    else:
                        answer+='L'
                        a1=a3
                        b1=b3
                        
    
    return answer

numbers=[1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
hand="right"
print(solution(numbers, hand))