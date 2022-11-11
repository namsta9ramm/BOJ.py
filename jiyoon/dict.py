f = open("C:/Users/david/OneDrive/바탕 화면/dict_test.TXT", 'r') #먼저 파일을 연다. 파일의 경로를 복붙해준다.
lines = f.readlines() # 한줄씩 읽는다
while True: #일단 계속 반복하는데
    m=input() #m이라는 변수에 문자를 입력받는다.
    for line in lines: # 딕셔너리를 보면 영문 : 뜻 형식으로 되어있다.
        a=line.split(":") # 영문과 뜻을 따로 추출해줘야 하기때문에 리스트를 분리해준다.
        a[0]=a[0].strip() #a[0].strip() 스트라이프를 하는이유는 공백을 제거해주기 위함이다.
        if str(m)==a[0]: #만약 같으면 
        
            print(a[0],a[1]) # 뜻을 출력해준다. 

        # 이 사전을 끝나지 않는 무한반복의 사전이다.
            
       
        