def solution(survey, choices):
    dict={"R":0,"T":0,"C":0,"F":0,"J":0,"M":0,"A":0,"N":0}
    new_ch=[]
    for k in choices:
        new_ch.append(k-4)
    for i in range(len(survey)):
        if new_ch[i]>0:
            dict[survey[i][1]]+=new_ch[i]
        elif new_ch[i]<0:
            dict[survey[i][0]]+=-new_ch[i]       
    answer = ''
    if dict["R"]>=dict["T"]:
        answer+='R'
    else:
        answer+='T'
        
    if dict["C"]>=dict["F"]:
        answer+='C'
    else:
        answer+='F'
    if dict["J"]>=dict["M"]:
        answer+='J'
    else:
        answer+='M'
    if dict["A"]>=dict["N"]:
        answer+='A'
    else:
        answer+='N'
    
    return answer
print(solution(["AN", "CF", "MJ", "RT", "NA"],[5, 3, 2, 7, 5]))