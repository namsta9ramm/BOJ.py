from collections import deque
F,S,G,U,D=map(int,input().split())
# (1 ≤ S, G ≤ F ≤ 1000000, 0 ≤ U, D ≤ 1000000) 
#반례 ) 1000000 1000000 1 0 1
check_list=[]
def bfs():
    q=deque()
    q.append(S)
    dict[S]=1  #여기
    check_list.append(S)
    while q:
        x=q.popleft()
        if x==G:
            print(dict[x]-1)  #여기
            break
            
        for i in (x+U,x-D):
            if 0<i<=F and not dict[i]:
                q.append(i)
                check_list.append(i)
                dict[i]=dict[x]+1
                    
dict=[0]*(F+1)
bfs()
if G not in check_list:
    print("use the stairs")

