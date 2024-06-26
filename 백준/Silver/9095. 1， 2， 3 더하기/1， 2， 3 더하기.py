import sys
import math

n = int(input())

count = [0 for i in range(12)]
count[1] = 1
count[2] = 2
count[3] = 4

for i in range(4,12) :
    count[i] = count[i-1]+count[i-2]+count[i-3]
for i in range(n) :
    print(count[int(sys.stdin.readline())])
