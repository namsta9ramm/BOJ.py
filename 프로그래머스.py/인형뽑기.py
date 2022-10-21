from collections import deque
board=[[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves=[1,5,3,5,1,2,1,4]
a=len(board)
new_board=[]

for i in range(a):
    board1=[]
    for j in range(a):
        if board[j][i]!=0:
            board1.append(board[j][i])
    new_board.append(board1)
new_list=[]
ans=0
for i in moves:
    print(new_board)
    what=new_board[i-1]
    if len(what)>0:
        k=what.pop(0)
        new_list.append(k)
        if len(new_list)>=2:
            if k==new_list[-2]:
                new_list.pop()
                new_list.pop()
                ans=ans+2
print(ans)