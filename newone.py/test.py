def solution(id_list, report, k):
    new_dict={}
    ans_dict={}
    use_set=set(report)
    report=list(use_set)
    for i in id_list:  # new_dict={"muzi":0 , "frodo":0 , "apeach":0 , "neo":0 }
        new_dict[i]=0   #repot =["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"]
    for i in id_list:
        ans_dict[i]=0
    for i in report:
        name,who=i.split()
        
        new_dict[who]+=1
                        # dict={"muzi":1 , "frodo":2 , "apeach":0 , "neo":2 }
                        # k를 넘은 것들 - frodo 와 neo를 뽑은 사람 l = ["frodo","neo"]
    l = [ q for q, v in new_dict.items() if v >=k ] 
    for m in report:
        name,who=m.split()
        if who in l:           
            ans_dict[name]+=1
    return list(ans_dict.values())    
    
print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo", "apeach frodo", "apeach neo", "muzi neo"], 1))
        
    