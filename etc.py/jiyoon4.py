#입력받는 숫자는 99,999 이하입니다 
# X만X천 X백 X십 X원
dict={'0':"",'1':"",'2':"이",'3':"삼",'4':"사",'5':"오",'6':"육",'7':"칠",'8':"팔",'9':"구"}
money=input()

if len(money)<=3:           #너무 노가다 문제, 먼저 입력한 숫자를 천단위로 끊어야 하니 입력한 돈의 자릿수에 따라 경우를 나눠서 출력한다 6~14줄
    print(money)            #딕셔너리를 선언해서 각 숫자에 해당하는 우리나라 말을 넣어둔다.
                            # 그 후 한국말을 출력하는 식도 위와 똑같이 입력한 돈의 자릿수를 1부터 5까지 경우의수를 나눠서 출력한다. 16~~ 줄
elif len(money)<=4:         # 중간 중간에 조건문에 num이 1이고 0 인 경우를 나눈것은 10,006같은 경우 만육원, 중간의 한국말을 말할 필요가 없기에
    print(money[:1]+","+money[1:]) # 그 자릿값이 0이면 한국말에 0을 곱해줌으로써 한국말을 없앤다.
elif len(money)<=5:
    print(money[:2]+","+money[2:])
elif len(money)<=6:
    print(money[:3]+","+money[3:])

if len(money)==1:
    print(dict[money]+"원")
elif len(money)==2:
    print(dict[money[0]]+"십"+dict[money[1]]+"원")
elif len(money)==3:
    if money[1]=='0':
        num=0
    else:
        num=1    
    print(dict[money[0]]+"백"+dict[money[1]]+num*"십"+dict[money[2]]+"원")
elif len(money)==4:
    if money[1]=='0':
        num=0
    else:
        num=1
    if money[2]=='0':
        num1=0
    else:
        num1=1     
    print(dict[money[0]]+"천"+dict[money[1]]+num*"백"+dict[money[2]]+num1*"십"+dict[money[3]]+"원")

elif len(money)==5:
    if money[1]=='0':
        num=0
    else:
        num=1
    if money[2]=='0':
        num1=0
    else:
        num1=1
    if money[3]=='0':
        num2=0
    else:
        num2=1      
    print(dict[money[0]]+"만"+dict[money[1]]+num*"천"+dict[money[2]]+num1*"백"+dict[money[3]]+num2*"십"+dict[money[4]]+"원")


