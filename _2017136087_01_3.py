import time # time모듈을 불러온다

def fib(n): # 순환 알고리즘을 이용한 피보나치 수열
    if n == 0:
        return 0    # 0번째 항 -> 0
    elif n == 1:
        return 1    # 1번째 항 -> 1
    else:
        return fib(n-1) + fib(n-2)  
        # n번째 항은 n-1번째와 n-2번째를 합한 값이라는 
        # 피보나치 수열의 정의에 입각한 반환형

def fib_iter(n):    # 반복 알고리즘을 이용한 피보나치 수열
    if n < 2 : 
        return n
    prev = 0
    curr = 1
    for e in range(2,n+1):  # 2부터 n 즉, n-1번 반복
        tmp = curr
        curr = curr + prev
        prev = tmp
        # n-1번째 항을 임시 공간에 저장한 뒤
        # 해당 항의 n-1번째 항과 n-2번째 항을 더하고
        # 임시공간에 저장한 값을 다음 항을 구할 때 n-2번째로 사용
    return curr

print('Fibonacci순환(6) =', fib(6))
print('Fibonacci반복(6) =', fib_iter(6))

for i in range(1,40):   # 1 ~ 39
    start = time.time()
    fib_iter(i)
    end = time.time()
    t1 = end - start
    # 반복 알고리즘 시간 측정
    
    start = time.time()
    fib(i)
    end = time.time()
    t2 = end - start
    # 순환 알고리즘 시간 측정

    print('n = ',i,'    반복: ',t1, ' 순환: ',t2)
