import sys

n = int(input())

tile = [0 for i in range(1001)]
tile[1] = 1
tile[2] = 2

# 귀납적으로 얻어낸 식 피보나치와 사실상 동일.
for i in range(3,n+1) :
    tile[i] = tile[i-1] + tile[i-2]
print(tile[n]%10007)
