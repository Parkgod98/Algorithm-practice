import sys

n = int(input())

stairs = [0]*301
cases = [0]*301
for i in range(1,n+1) :
    stairs[i] = int(sys.stdin.readline())
cases[1] = stairs[1]
cases[2] = stairs[1]+stairs[2]
cases[3] = max(stairs[1]+stairs[3],stairs[2]+stairs[3])

for i in range(4,n+1) :
    cases[i] = max(cases[i-3]+stairs[i-1]+stairs[i],cases[i-2]+stairs[i])
print(cases[n])