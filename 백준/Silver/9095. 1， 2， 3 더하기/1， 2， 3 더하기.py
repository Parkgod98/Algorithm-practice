import sys
import math

n = int(input())

count = [0 for i in range(12)]
# 초기 경우의 수 입력.
count[1] = 1
count[2] = 2
count[3] = 4

# 다음 경우의 수를 만드는 법은 직전 3개의 합과 같음. 경험적,귀납적으로 얻어낸 결과.
for i in range(4,12) :
    count[i] = count[i-1]+count[i-2]+count[i-3]
# 단순 출력.
for i in range(n) :
    print(count[int(sys.stdin.readline())])
