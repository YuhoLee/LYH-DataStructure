def sum(n): # 1부터 n까지의 합을 구하는 순환 알고리즘
    print(n)
    if n < 1:
        return 0;
    else:
        return n + sum(n-1) # 재귀 호출

def asterisk(i):    # 별을 출력하는 순환 알고리즘
    if i > 1:
        asterisk(i/2)
        asterisk(i/2)
    print("*",end='')
    # asterisk(i)가 호출 될 때, i가 1보다 클 시 asterisk(i/2)를 두번 호출한다.


print('sum(5)의 실행결과:',sum(5),'\n')  # 5+4+3+2+1
asterisk(5) # 총 15개의 별이 출력.
print('\n')

