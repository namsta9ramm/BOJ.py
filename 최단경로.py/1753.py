#다익스트라 알고리즘
#첫째줄에 정점의 개수 V와 간선의 개수 E가 주어집니다.
#두번째 줄에는 시작정점의 번호 k가 주어진다.
#세번째 줄부터 E개의 줄을 거쳐 간선을 나타내는 세 정수가 나타난다.

lnf=int(1e9)
n, m = map(int, input().split())
start=int(input()) #시작정점의 번호
graph=[[] for _ in range(n+1)]
visited=[False]*(n+1) #방문처리 기록용
distance=[lnf]*(n+1) #거리 테이블용

for _ in range(m):
    q,w,e=map(int,input().split())
    graph[q].append(w,e)

#방문하지 않은 노드이면서 시작노드와 최단거리인 노드 반환
#선형탐색, 가장쉬운 구현법
def get_smallest_node():
    min_value=lnf
    index=0
    for i in range(1,n+1):
        if not visited[i] and distance[i]<min_value:
            min_value=distance[i]
            index=i
    
    return index


