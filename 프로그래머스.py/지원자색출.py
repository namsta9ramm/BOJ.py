infos=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

querys=["java and backend and junior and pizza 100","python and frontend and senior and chicken 200","cpp and - and senior and pizza 250","- and backend and senior and - 150","- and - and - and chicken 100","- and - and - and - 150"]

ans_list=[]
for i in range(len(infos)):
        info = infos[i]  #info="java backend junior pizza 150" 
        info = info.split(' ') #info=["jave","backend","junior","pizz","150"]
        info = list(map(lambda x: int(x) if x.isnumeric() else x[0], info))
        infos[i] = info
for i in range(len(querys)):
        query = querys[i]
        query = query.replace(' and', '')
        query = query.split(' ')
        query = list(map(lambda x: int(x) if x.isnumeric() else x[0], query))
        querys[i] = query

for component in querys: #component=["j","b","j","p","100"]
        n=0
        for i in infos:
                flag1=False 
                for j in range(4):
                        if component[j]!='-' and component[j]!=i[j]:
                                break
                        if j==3:
                                flag1=True
                if flag1 and i[4]>=int(component[4]):
                        n=n+1
       
        ans_list.append(n)
print(ans_list)