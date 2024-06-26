import sys

def dfs(v) :
    visited[v] =1 # 방문 표시.
    for nx in graph[v] : # 연결된 모든 노드들에 대해서 반복하며
        if visited[nx] == 0 : # 아직 방문하지 않은 노드일때
            dfs(nx)           # 방문한다.

n = int(input())
v = int(input())

graph = [[] for i in range(n+1)] # 1번부터 n번 컴퓨터까지. 0번 인덱스는 사용 X
visited =[0]*(n+1) # 일단 다 방문하지 않은것으로 가정.

# 무엇이 연결되어 있는지 입력받는다.
for i in range(v) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b) # a번 컴퓨터에 b가 연결되어있다.
    graph[b].append(a) # b번 컴퓨터에 a가 연결되어 있다.
    
dfs(1) # 1번과 연결된것들을 찾아보자.
visited[1] = 0 # 1번 자신은 제외.
print(visited.count(1)) # 1번을 타고 들어갔을때 방문된 노드들의 갯수.
