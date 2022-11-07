a=int(input())
list1=list(map(int,input().split()))
num=int(input())

ans=0
for i in list1:
    if i ==num:
        ans=ans+1

print(ans)