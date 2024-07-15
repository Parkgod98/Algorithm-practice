import sys

t = []

def Comb(k,depth,start) :
    if depth == k :
        print(*t)
        return
    for i in range(start,n) :
        t.append(nums[i])
        Comb(k,depth+1,i)
        t.pop()


n,k = map(int,sys.stdin.readline().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
Comb(k,0,0)
