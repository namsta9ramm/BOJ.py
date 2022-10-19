from bisect import bisect_left
from itertools import combinations

def make_all_cases(separate_info):  #모든 테스트 케이스를 만드는 함수, 
    cases = []                      #결국 모든 경우의수를 다 만든다음 비교를 하는게 효율성을 만족한다.
    for k in range(5):
        for condition in combinations([0,1,2,3], k):
            case = []
            
            for idx in range(4):
                if idx not in condition:
                    case.append(separate_info[idx])
                else:
                    case.append('-')
            cases.append(''.join(case))
    return cases

def solution(info, query):
    answer = []
    all_people = {}
    for i in info:
        seperate_info = i.split()
        cases = make_all_cases(i.split())
        for case in cases:  # 딕셔너리에 모든 경우의수에 해당하는 점수들을 저장
            if case not in all_people.keys(): 
                all_people[case] = [int(seperate_info[4])]
            else: 
                all_people[case].append(int(seperate_info[4]))
    
    for key in all_people.keys(): #Binary Search 를 위한 사전 정렬
        all_people[key].sort()
    
    for q in query:
        seperate_q = q.split()
        target = seperate_q[0] + seperate_q[2] + seperate_q[4] + seperate_q[6]
        if target in all_people.keys(): # Binary Search 를 사용해야 시간 효율성 증가
            answer.append(len(all_people[target]) - bisect_left(all_people[target], int(seperate_q[7]), lo=0, hi=len(all_people[target])))
        else:
            answer.append(0)

    return answer
