a=input()  
list1=a.split("+")              # ex) 334+123-32+245-6-32 를 계산해야 할때 +를 기준으로 문자열을 나눈다 
ans_list=[]                     # 그러면 ["334","123-32","245-6-32"] 가 됩니다.
for i in list1:    
    list2=i.split("-")          # 이걸 또 반복문으로 하나씩 돌면서 - 기준으로 문자열을 나눕니다
    num=int(list2[0])

    for j in range(1,len(list2)): # 이 과정 안에서 빼기를 계산해줍니다 ( 빼기 계산과정이 이해하기 어려울 수 있음 )
        num=num-int(list2[j])   #그러면 결국 ans_list에는 [334,91,207] 이 남는다.
    ans_list.append(num)        # 모든 리스트 안의 인수를 더해주면 정답을 리턴한다
ans=ans_list[0]
for k in range(1,len(ans_list)):
    ans=ans+ans_list[k]
print(ans)

