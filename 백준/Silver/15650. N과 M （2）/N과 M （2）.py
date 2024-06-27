import sys
# 조합 논리. nCm
n,m = map(int,sys.stdin.readline().split())

base = [i for i in range(1,n+1)] # 조합을 수행할 배열
example =[]

# 배열 내 요소 띄어쓰기 출력.
def PrintList(arr):
    for i in arr :
        print(i ,end =' ')
    print("")
# 조합 함수.
def Comb(base,start,n,m) :
    # m개를 고르고나면 프린트.
    if len(example) == m :
        PrintList(example)
        return
    for i in range(start+1,n) :
        example.append(base[i])
        Comb(base,i,n,m)
        example.pop()
    return
Comb(base,-1,n,m)