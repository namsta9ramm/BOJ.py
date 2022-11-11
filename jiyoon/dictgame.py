import random   #푸는데 상당히 오래걸린 문제
import time   
f = open("C:/Users/david/OneDrive/바탕 화면/dict_test.TXT", 'r') #먼저 사전 문제와 동일하게 파일을 열어줍니다.
lines = f.readlines()
list1=[]
for line in lines:
    a=line.split(":")
    a[0]=a[0].strip()
    list1.append(a[0])  #주어진 사전데이터 전처리, 영문으로만 구성되어있는 새로운 리스트를 만들어줍니다. 우리가 필요한건 영문만 필요하기 때문에
print("게임을 시작합니다.")
sum=0  #총 합계를 선언합니다.
for i in range(1,11): #총 10번의 게임을 실행 
  
    num=random.randint(7,10) #7부터 10까지의 난수(무작위의 숫자)를 생성합니다.
    out=random.sample(list1,num) #sample이라는 모듈은 리스트(list1)에서 num개수만큼의 영문 단어를 추출해주는 모듈입니다. out에 저장해줍니다. 
    print("("+str(i)+"/10) 다음을 입력하세요")
    a=''
    for k in out:
        print(k,end=" ") #지금 현재 out은 리스트 형식으로 저장되어있기 떄문에 ' ~ ~  ' 처럼 문자열 형식으로 바꿔줍니다.
        a=a+str(k)
        a=a+' '
    a=a[:-1]   #문자열 마지막에 공백이 하나 들어감으로 마지막 공백 하나를 삭제해줍니다.
    print('')
    start = time.time() #여기서 시간변수를 설정하게 되는데 여기서 부터 타이머를 누른거고.
    b=input()
    end = time.time() # 여기서 타이머를 종료하는겁니다. 즉 input() 하는 동안의 시간을 재는 모듈입니다.
    ans=''
    for i in range(len(b)): #여기서는 만약 틀릴경우에 대해서 코드를 짜는 부분인데 
        if str(a[i])==str(b[i]): 
            ans=ans+' ' #맞는 부분은 공백으로 넘어가고
        else:
            ans=ans+("^") # 만약 문자가 다른 부분이 발견될 경우에 문자 ^를 추가해주고 반복문을 종료한다. 더이상 실행할 필요가 없기 때문입니다.
            break
    if str(a)==str(b): #만약 문자 두개가 같다면
        
        sec = (end - start) #시간을 계산하고 
        sec=round(sec) #반올림 한 후 점수 계산을 해주면 끝난다.
        print("맞았습니다"+" ("+str((20-sec)*1000)+"점 획득  "+str((20-sec)*1000)+"타/분)")
        sum=sum+(20-sec)*1000
        
    else:       #만약 두 문자가 다르다면 아까 다를 경우에 출력해줄 문자를 만든것을 출력해주고 타자수만 출력해준다.
        print(ans)
        print("틀렸습니다"+str((20-sec)*1000)+"타/분)")

print("당신의 점수는 "+str(sum)+"점 입니다.")#마지막에는 총점을 출력해주고 마무리한다.