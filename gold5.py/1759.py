import sys
def back_tracking(cnt, idx):
    # 암호를 만들었을 때
    if cnt == a:
        
        vo, co = 0, 0
        for i in range(a):
            if answer[i] in 'aeiou':
                vo += 1
            else:
                co += 1
        # 모음 1개,자음 2개 이상
        if vo >= 1 and co >= 2:
            print("".join(answer))
        return
    # 반복문을 통해 암호를 만든다.
    for i in range(idx, b):
        answer.append(words[i])
        back_tracking(cnt + 1, i + 1) 
        answer.pop()

a, b = map(int,input().split())    # a=4 b=6
words =input().split()  # words= a t c i s w - > sorted words= a c i t s w 
words.sort()
answer = []
back_tracking(0, 0)