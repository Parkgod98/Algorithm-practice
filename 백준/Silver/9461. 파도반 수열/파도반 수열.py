import sys

def GetTri(n) :
    tri = [0, 1, 1, 1, 2, 2, 3, 4, 5, 7, 9]
    if n > 10 :
        for i in range(11,n+1) :
            tri.append(tri[i-2]+tri[i-3])
    return tri[n]


n = int(input())

for i in range(n) :
    print(GetTri(int(sys.stdin.readline())))