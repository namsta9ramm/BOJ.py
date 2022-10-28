def solution(ingredient):
    ans_list=''
    answer = 0
    for i in ingredient:
        ans_list+=str(i)
        if '1231' in ans_list:
            ans_list=ans_list.replace("1231","")
            answer+=1
    
    return answer

print(solution([1,1,1,1,2,3,1,1,1,1,1,1]))