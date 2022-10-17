def solution(new_id):
    
    j=''
    for i in new_id:
        i=str(i)
        if i=='-' or i=='_' or i=="." or i.isnumeric():
            j=j+i
        elif i.isalpha():
            i=i.lower()
            j=j+i 
    
    while True: 
        if ".." not in j:
            break
        else:
            j=j.replace("..",".")
    if len(j)==1:
        j=j.lstrip(".")
    
    else:
        if j[0]==".":
            j=j.lstrip(".")
        elif j[-1]==".":
            j=j.rstrip(".")
    
    if j=="":
        j="a"
        
    if len(j)>=16:
        j=j[:15]
        if j[-1]==".":
            j=j.rstrip(".")
    
    
    while len(j)<=2:
        j=j+j[-1]    
    
    return j
print(solution("=.="))