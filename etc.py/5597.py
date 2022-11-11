list1=[]
for i in range(1,31):
    list1.append(i)
for i in range(28):
    
    a=int(input())
    list1.remove(a)
list1.sort()
for i in list1:
    print(i)