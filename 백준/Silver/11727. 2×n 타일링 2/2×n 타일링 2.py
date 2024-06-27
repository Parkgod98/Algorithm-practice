import sys

case = [0,1,3,5]
n = int(input())

for i in range(4,n+1) :
    if i%2 == 0 :
        case.append(case[i-1]*2+1)
    else:
        case.append(case[i - 1] * 2 - 1)
print(case[n]%10007)
