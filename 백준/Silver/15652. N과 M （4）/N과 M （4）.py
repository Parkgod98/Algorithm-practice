# 숫자 리스트 만들고 인덱스로 접근
# 숫자 리스트 생성
# num_list = [i for i in range(1,n+1)]

# def Comb(k,depth,index) :
#     if depth == k :
#         print(t)
#         return
#     for i in range(index,n) :
#         t.append(num_list[i])
#         Comb(k,depth+1,i)
#         t.pop()

# 숫자 리스트 없이 썡으로 접근
def Comb(k,depth,index) :
    if depth == k :
        print(*t)
        return
    for i in range(index,n) :
        t.append(i+1)
        Comb(k,depth+1,i)
        t.pop()
# 입력 받기
n,k = map(int,input().split())
t = []
Comb(k,0,0)