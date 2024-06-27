import sys

# 귀납적으로 n-2번째항과 n-3번째 항의 합이 n번쨰 항과 같은것을 발견했고 
# 다이나믹 프로그래밍으로 해결
n = int(input())
p = [0,1,1,1,2,2]

for i in range(6,101) :
    p.append(p[i-2]+p[i-3])

for i in range(n) :
    N = int(sys.stdin.readline())
    print(p[N])
