tel={'홍길동':'010-4444-5555','김중앙':'010-9191-8181','심청':'010-3232-5454'}  
while True :
    use_num=0     # use_num 이라는 매개변수 설정
    name=input('이름은?')
    
    if name == 'add':   # 만약에 이름이 add면 
        newname= input('이름은? ')
        newnumber= input('전화번호는? ')
        tel[newname] = newnumber   # 이름과 전화번호를 물어본 후, 딕셔너리 tel에 추가 
        print(newname," 전화번호가 추가되었습니다")

    else:
        for i in tel.keys():   # tel 에서 키 값만 추출  ex) ['홍길동','김중앙','심청']  ,  i에는 홍길동 , 김중앙 , 심청이 차례로 들어감
            if name in i:      # 만약 name 입력값이 i 안에 포함되어있을 시 ex) name=홍길, i=홍길동 - >  True   name=지윤, i=홍길동 ->false                 
                print(tel[i])  # i에 해당되는 값을 출력
                use_num+=1     # use_num 매개변수 값을 하나 증가시킴
        if use_num==0:         # for 문을 다돌았는데 매개변수 값이 0이면 - > 모든 이름을 탐색했는데 내가 입력한 이름이 포함되는게 없다
            print("그런사람없어요.") # 그런 사람은 없다고 출력 
