p=["mislav", "stanko", "mislav", "ana"]
c=["stanko", "ana", "mislav"]
dict1={}

for i in p:
    if i in dict1:
        dict1[i]=dict1[i]+1
    else:
        dict1[i]=1

for j in c:
    if j in dict1:
        dict1[j]=dict1[j]-1

for k in dict1.keys():
    if dict1[k]!=0:
        print(k) 