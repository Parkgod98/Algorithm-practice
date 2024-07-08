import sys
# 중요도 리스트 생성.
def GetList(n) :
    return list(map(int,sys.stdin.readline().split()))
# Test case 갯수
N = int(input())

for i in range(N) :
    count = 0 # 몇번쨰로 출력될지
    n,index = map(int,sys.stdin.readline().split()) # 갯수와 타겟 인덱스 입력받음.
    q = GetList(n) # 받은 정보 기반 리스트 생성.
    while True :
        if q[0] < max(q) : # 중요도가 낮은게 맨 앞에 있다면
            q.append(q.pop(0)) # 뺴고 바로 뒤에 append
            if index == 0 : # index 추적.
                index = len(q)-1
            else : # index 추적.
                index -=1
        else : # 중요도 제일 큰게 맨 앞
            q.pop(0)  # 바로 출력
            count += 1 # 출력횟수 증가
            if index == 0 : # 맨앞이 타겟 인덱스였다면
                print(count) #
                break
            else :
                index -=1
