import sys

def dfs(m,stack,visited) :
    if len(stack) == m :
        print(' '.join(map(str,stack)))
        return
    for i in range(1,n+1) :
        if visited[i] == False :
            visited[i] = True
            stack.append(i)
            dfs(m,stack,visited)
            stack.pop()
            visited[i] = False

n,m = map(int,sys.stdin.readline().split())

visited =[False for i in range(n+1)]
stack =[]
dfs(m,stack,visited)