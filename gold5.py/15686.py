from itertools import combinations
a,b=map(int,input().split())
allmap=[]
chick=[]
house=[]
for _ in range(a):
    allmap.append(list(map(int,input().split())))

for i in range(a):
    for j in range(a):
        if allmap[i][j]==1:
            house.append((i,j)) #가정집 위치 입력
        elif allmap[i][j]==2:
            chick.append((i,j)) #치킨집 위치 입력
list_1=list(combinations(chick,b)) #치킨집 개수 조합

ans_list=[]
for i in list_1: #ex) (1,0) 
    ans=0
       
    for j in range(len(house)):
        num=10000         
        for x,y in i: # x=1 y=0
            num=min(num,abs(x-house[j][0])+abs(y-house[j][1]))
        ans=ans+num
    
    ans_list.append(ans)
print(min(ans_list))