import sys

N = int(input())
# 구해보니 피보나치더라.
dp = [i for i in range(91)]
dp[0] = 0
dp[1] = 1
dp[2] = 1
for i in range(3,91) :
    dp[i] = dp[i-1]+dp[i-2]
print(dp[N])