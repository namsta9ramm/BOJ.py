sum=0
list1=[]
for i in range(5):
    k=int(input())
    list1.append(k)
    sum=sum+k
list1.sort()
print(sum//5)
print(list1[2])