import sys

N = int(input())
num_list = []
avg = 0
num_dict ={}
# 입력
for i in range(N) :
    num_list.append(int(sys.stdin.readline()))
    avg+=num_list[i]
    if num_list[i] not in num_dict :
        num_dict[num_list[i]] = 1
    else :
        num_dict[num_list[i]] +=1
# 가공
new = sorted(num_dict.items(), key=lambda x:(-x[1],x[0]))
num_list.sort() # 받은 숫자 sort
# 얻어내기
avg /= N
mid = num_list[len(num_list)//2]
rng = num_list[-1] - num_list[0]
max_num = new[1][0] if len(new) >=2 and new[0][1] == new[1][1] else new[0][0]
# 출력
print(round(avg))
print(mid)
print(max_num)
print(rng)