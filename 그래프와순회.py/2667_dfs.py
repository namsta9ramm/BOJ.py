#정사각형 모양의 지도가 있다.
#단지에 속하는 집의 수를 오름차순으로 정렬후 출력
#N개의 집, 그 안에 속하는 집의 개수 차레대로 출력
#dfs 풀이

a=int(input())
graph1=[]
for _ in range(a):
    graph1.append(list(map(int,input())))
cnt=0
graph2=[]
dx=[-1,1,0,0]
dy=[0,0,-1,1]

def dfs(x,y):
    global cnt 
    if x<0 or y<0 or x>=a or y>=a:
        return False
    if graph1[x][y]==1:
        cnt=cnt+1
        graph1[x][y]=0
        for i in range(4):
            dfs(x+dx[i],y+dy[i])
        return True
for i in range(a):
    for j in range(a):
        if dfs(i,j)==True:
            graph2.append(cnt)
            cnt=0

print(len(graph2))
graph2.sort()
for i in graph2:
    print(i)



