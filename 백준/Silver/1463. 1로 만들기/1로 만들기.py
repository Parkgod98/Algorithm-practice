n = int(input())
count =[0 for i in range(n+1)] # 1부터 n까지. 횟수담을 배열.

for i in range(2,n+1) :
    count[i] = count[i-1]+1 # 다음 항은 +1해서 가는것. 
    if i%3 == 0 :
        # 직전에서 1을 더해서 온것과, 3을 곱해서 온것중 뭐가 더 빠른지를 판단
        count[i] = count[i] if count[i] < count[i//3] +1 else count[i//3] +1 
    if i%2 == 0 :
        count[i] = count[i] if count[i] < count[i//2] +1 else count[i//2] +1

print(count[n])
