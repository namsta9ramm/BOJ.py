list1=list(map(int,input().split()))
a=len(list1)
b=max(list1)
ans=0
for i in range(b):
    
    for j in range(a):
        flag1=False
        flag2=False
        
        if list1[j]<=0:
            list2=list1[:j]
            list3=list1[j:]
           
            for n in list2:
                if n>0:
                    flag1=True
            for m in list3:
                if m>0:
                    flag2=True 
            if flag1 and flag2:
                ans=ans+1       
            
    for k in range(a):
        list1[k]=list1[k]-1

print(ans)