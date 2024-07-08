import sys
# 입력 받기
N,M = map(int,input().split())
num_list = list(map(int,sys.stdin.readline().split()))

# 누적 합 리스트 생성
cumulative_sum_list = [0]
for i in range(len(num_list)) :
    cumulative_sum_list.append(num_list[i]+cumulative_sum_list[i])

# j번쨰에서 i-1번쨰를 빼면 i~j까지의 합
for _ in range(M) :
    i,j = map(int,sys.stdin.readline().split())
    print(cumulative_sum_list[j]-cumulative_sum_list[i-1])