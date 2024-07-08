import sys

def Comb(k,depth) :
    if depth == k :
        print(*t)
        return
    for i in range(n) :
        if nums[i] not in t :
            t.append(nums[i])
            Comb(k,depth+1)
            t.pop()

n,k = map(int,input().split())
nums = list(map(int,sys.stdin.readline().split()))
nums.sort()
t = []

Comb(k,0)
