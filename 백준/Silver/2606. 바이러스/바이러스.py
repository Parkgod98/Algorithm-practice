import sys

def dfs(v) :
    visited[v] =1
    for nx in graph[v] :
        if visited[nx] == 0 :
            dfs(nx)

n = int(input())
v = int(input())

graph = [[] for i in range(n+1)]
visited =[0]*(n+1)

for i in range(v) :
    a,b = map(int,sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)
    
dfs(1)
visited[1] = 0
print(visited.count(1))