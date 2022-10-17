info="java backend junior pizza 150"
infos=["java backend junior pizza 150","python frontend senior chicken 210","python frontend senior chicken 150","cpp backend senior pizza 260","java backend junior chicken 80","python backend senior chicken 50"]

for i in range(len(infos)):
        info = infos[i]  #info="java backend junior pizza 150" 
        info = info.split(' ')
        info = list(map(lambda x: int(x) if x.isnumeric() else x[0], info))
        infos[i] = info

print(infos)