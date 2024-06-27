import sys
'''
외접은 R+r = d 일때고, 내접은 R-r = d 일때임. 즉 외접과 내접의 사이에 존재하는
R-r < d < R+r 일때가 두 점에서 만나는 상황이라고 할수 있음.
이를 제외한 모든 상황은 크기가 같은 동심원을 제외하고 서로 만나지 않는 두 원임.
'''

def Classification(x1,y1,r1,x2,y2,r2) :
    # 중심 거리 계산
    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
    if x1 == x2 and y1 == y2 and r1 == r2: # 크기가 같은 동심원
        return -1
    elif r1+r2 == distance or abs(r1-r2) == distance : # 외접, 내접
        return 1
    elif r1+r2 > distance and distance > abs(r1-r2): # 두점에서 만날때
        return 2
    else :
        return 0

T = int(input())

for i in range(T) :
    x1,y1,r1,x2,y2,r2 = map(int,sys.stdin.readline().split())
    print(Classification(x1,y1,r1,x2,y2,r2))
