def solution(info, query):
    answer = []
    for q in query:
        orders = q.split()
        cnt = 0
        for i in info:
            people = i.split()
            if orders[0] != "-":
                if orders[0] != people[0]:
                    continue
            if orders[2] != "-":
                if orders[2] != people[1]:
                    continue
            if orders[4] != "-":
                if orders[4] != people[2]:
                    continue
            if orders[6] != "-":
                if orders[6] != people[3]:
                    continue
            if int(people[4]) >= int(orders[7]):
                cnt += 1
        answer.append(cnt)
    return answer
    #["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]
    #["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]
