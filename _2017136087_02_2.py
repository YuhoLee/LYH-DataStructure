import random
#랜덤 숫자를 생성하거나 다양한 랜덤 관련 함수를 제공하는 모듈

min = 0
max = 99
flag = 0
answer = random.randrange(0,100)    # 0부터 99까지의 난수를 발생시킨 뒤, answer에 저장한다

for i in range(1,11):   # 기회를 10번 부여하기 때문에 구간을 range(1,11)로 설정
    print("숫자 입력(범위: %d~%d): "%(min,max),end = '')
    guess = int(input())
    if(answer > guess):
        print(" 틀렸습니다. 더 큰 숫자입니다!\n")
        min = guess
    # 정답이 추측보다 커서 메세지를 출력하고 추측 값을 최소로 함

    elif (answer < guess):
        print(" 틀렸습니다. 더 작은 숫자입니다!\n")
        max = guess
    # 정답이 추측보다 작아서 메세지를 출력하고 추측 값을 최대로 함

    else:
        print(" 정답입니다!! ",i,"번 만에 맞췄네요~~")
        flag = 1
        break
    # 정답을 맞추면 메세지를 출력하고 flag를 1로 설정한 후 반복문 탈출

if (flag != 1):
    print("----- 시도 횟수 초과 -----")
# 정답 조건의 flag = 1을 거치지 않은 경우는 정답을 못맞힌 채 
# 횟수 초과로 인해 반복문을 탈출한 경우이기 때문에 횟수 초과 메세지 출력

print("\n게임 끝!!")
