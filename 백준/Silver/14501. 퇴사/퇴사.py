import sys

def Allprofit(day,profit) :
    global max_profit
    # 내 날을 넘어가면 종료
    if day >= N :
        max_profit = max(max_profit,profit)
        return
    # 현재 날을 선택하지 않는 경우.
    Allprofit(day+1,profit)
    # 현재 날을 선택하는 경우
    if day + node[day][0] <= N : # 단 상담을 한게 바운더리 안에 있어야함.
        Allprofit(day+node[day][0],profit+node[day][1])


N = int(input())

node = []
for _ in range(N) :
    n = list(map(int,sys.stdin.readline().split()))
    node.append(n)

max_profit = 0
Allprofit(0,0)
print(max_profit)
