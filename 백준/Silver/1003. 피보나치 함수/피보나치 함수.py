import sys

zero = [0 for i in range(41)] # 0이 몇번 호출됐는지 담을 배열.
one = [0 for i in range(41)] # 1이 몇번 호출됐는지 담을 배열
# 초기값 배정.
zero[0] = 1 
zero[1] = 0
one[0] = 0
one[1] = 1

# 문제 조건상 가능한 모든 경우에 대한 0,1 호출 횟수 배열 생성.
for i in range(2,41) :
    zero[i] = zero[i-1] +zero[i-2]
    one[i] = one[i-1] + one[i-2]

n = int(input())
for i in range(n) :
    k = int(sys.stdin.readline())
    print(zero[k],one[k])
