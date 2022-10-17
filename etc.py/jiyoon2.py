a=input() #홍길동입니다. 생년월일은 20011006입니다.
ans=''
for i in a:
    i=str(i)   #내가 입력한 문장을 한글자씩 탐색하는데
    if i.isnumeric(): #만약에 내가 숫자를 발견했으면 // isnumeric() 함수는 숫자인지 판별해주는 함수
        ans+=i     # ans라는 새로운 문자열에 숫자를 추가
                   # 결국 ans는 20011006 , 문자열 슬라이싱을 통해 형식에 맞춰 출력
if len(ans)==8:    
    print(ans[:4]+"/"+ans[4:6]+"/"+ans[6:8])
else:    #원래 코드는 9줄에서 끝나야 하는데, 문제를 보면//제 이름은 홍길동이고 2001년 10월 6일에 태어났습니다 를 20011006 으로 출력함 
    list1=a.split("월")   # 그말은 6일을 06일로 채워야한다는 말인데
    for i in list1:       # 숫자가 7개면 -> 월이나 일 중에 하나가 한자리수
        ans1=''           # 월을 기준으로 문자열을 나눈 후 월이 한자리수인지, 일이 한자리 수인지 판별 해주고 그에 따라서 출력해줌
        for j in i:
            if j.isnumeric():
                ans1+=j
        if len(ans1)==5:
            print(ans1[:4]+"/"+ans1[4:5],end="/")
        elif len(ans1)==6:
            print(ans1[:4]+"/"+ans1[4:6],end="/")
        
        elif len(ans1)==2:
            print(ans1)
        elif len(ans1)==1:
            print("0"+ans1)
