def Comb(k,depth,index) :
    if k == depth :
        print(*t)
        return
    for i in range(index,n) :
        t.append(i+1)
        Comb(k,depth+1,index)
        t.pop()

n,k = map(int,input().split())
t = []
Comb(k,0,0)