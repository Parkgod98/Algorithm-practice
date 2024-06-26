import sys
n,x  = map(int,sys.stdin.readline().split())
list = list(map(int,sys.stdin.readline().split())) #파이썬은 N번만 입력받고 종료하는법이 없나?
for i in range(n) :
    if list[i] < x :
        print(list[i],end =' ')