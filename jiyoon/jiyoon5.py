letsplaygame="apple"        #제일 논리적으로 이해가 힘들 수 있는 문제 
i=1                         # 먼저 apple이라는 단어로 끝말잇기를 시작한다. 게임을 10회 진행한다고 하였으니 while 문에 i<=10 조건을 달고 시작한다.
ans=0                       # 만약 letsplaygame[-1]==a[0], 주어진값과 입력한 값의 끝과 시작이 같으면 점수를 1점 올리고 게임횟수인 i도 1점 올린다.
check_list=[]               # 그 후 기존에 있던 값인 letsplaygame에 내가 입력한 a를 넣어줌으로써 기존의 단어를 새로운 단어로 초기화시켜준다. 
                            # 그 후 check_list에 내가 입력한 단어를 넣는데 이것은 이미 나온 단어를 확인해줄 수 있는 리스트를 만들기 위함이다.
while i<=10:
    a=input("단어("+letsplaygame+"):")
    if a not in check_list:  # 나온단어가 아니면 진행  
        if letsplaygame[-1]==a[0]: #기존의 단어 마지막 알파벳과 새로운 단어의 제일 앞 알파벳이 같을 경우
            letsplaygame=a   # 핵심  ! !!    !!!  ! ! 이해가 어려울 수 있음
            ans=ans+1
            i=i+1
            print("1점 획득."+" 현재 점수"+str(ans)+" 점")
            check_list.append(a)
        
        else:
            ans=ans-1
            i=i+1
            print("끝말잇기가 안됩니다. 1점 차감"+" 현재 점수"+str(ans)+" 점")
        
    else:           # 나온 단어를 또 입력했다면 점수를 차감한다.
        ans=ans-1
        i=i+1
        print("이미 나온 단어입니다. 1점 차감"+" 현재 점수"+str(ans)+" 점")
    