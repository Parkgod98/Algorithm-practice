import sys

N = int(input())
# 구해보니 귀납이더라.
dp = [0,1,2]
for i in range(3,N+1) :
    dp.append((dp[i-1]+dp[i-2])%15746) # 이렇게 해야 이 값이 저장되는 곳의 메모리를 아낄수 있겠다.
print(dp[N])