# 소수
def Get_Prime(n) :
    '''각 숫자가 소수인지 아닌지 판단하는 배열 생성 0(False),1(False),2(True)
    2 이후엔 일단 소수라고 한다.'''
    is_prime = [False,False] + [True]*(n-1) 
    primes = []
    for i in range(2,n+1) :
        if is_prime[i] : # 소수라면
            primes.append(i) # 소수 배열에 삽입
            for j in range(i*2,n+1,i) :  # 에라토네스의 체.
                is_prime[j] = False # i의 배수는 전부 소수가 아니다.
    return primes # 소수 배열 반환

m,n = map(int,input().split()) # 정수 범위 입력 받기

primes = Get_Prime(n) 

for i in primes : 
    if i >= m : # m 이상의 소수 전부 출력
        print(i)
