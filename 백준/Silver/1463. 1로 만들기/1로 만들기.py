import sys
import math

n = int(input())
count =[0 for i in range(n+1)] # 1부터 n까지. 횟수담을 배열.

for i in range(2,n+1) :
    count[i] = count[i-1]+1 # 이새끼는 일단 우긴다.
    if i%3 == 0 :
        count[i] = count[i] if count[i] < count[i//3] +1 else count[i//3] +1 # 비교.
    if i%2 == 0 :
        count[i] = count[i] if count[i] < count[i//2] +1 else count[i//2] +1

print(count[n])
