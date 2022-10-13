from collections import deque
n,k=map(int,input().split())
maxnum=100000
dict=[0]*(maxnum+1)
move=[0]*(maxnum+1)
q=deque()
q.append(n)
while q:
        x=q.popleft()
        if x==k:
            print(dict[x])           
            break
        for i in (x-1,x+1,2*x):
            if 0<=i<=100000 and dict[i]==0:
                dict[i]=dict[x]+1
                q.append(i)
                move[i]=x
# dict x =3 
# move_list append(k) 마지막
# move_list append(n) 처음 
# for _ in range(2) k=move[k]=8 , k=move[8]=4 , k=move[4]
move_list=[]
move_list.append(k)        
for _ in range(dict[x]-1):
    k=move[k]
    move_list.append(k)
move_list.append(n)

move_list.reverse()
for i in move_list:
    print(i,end=" ")




