import sys
import math

rec = [0,1,3,5,11,21]

n = int(input())
for i in range(6,n+1) :
    if i%2 == 0 :
        rec.append(4*rec[i-2]-1)
    else :
        rec.append(4*rec[i-2]+1)
print(rec[n]%10007)