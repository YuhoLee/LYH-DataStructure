def contains(bag,e): # 리스트 bag에 e가 있는지 확인하는 함수
    return e in bag  
    # A in B : B에 A가 있는지 확인한 후 있으면 True, 없으면 False 반환

def insert(bag,e):  # 리스트 bag에 e를 추가하는 함수
    bag.append(e)   # append 메소드를 사용하여 리스트 가장 뒤에 추가

def remove(bag,e):  # 리스트 bag에서 e를 삭제하는 함수
    bag.remove(e)   # remove 메소드를 통해 e 삭제
        
def count(bag): # 리스트 bag의 원소개수를 반환하는 함수
    return len(bag) # len함수를 통해 리스트의 길이를 알아냄

def numOf(bag,item):    # 리스트bag에 들어있는 item의 개수 반환
    n = 0
    for s in bag :  # 리스트 bag의 성분들을 모두 조사하여
        if s == item:
            n = n + 1
        # item과 일치할 시, n의 카운트 1 증가
    return n


PyBag = []  # PyBag이라는 리스트 생성
insert(PyBag, '사과') # 사과 추가
insert(PyBag, '자두') # 자두 추가
insert(PyBag, '복숭아')    # 복숭아 추가
insert(PyBag, '파인애플')   # 파인애플 추가
insert(PyBag, '배')   #배 추가
print("가방속의 물건: ", PyBag)

insert(PyBag, '복숭아')    # 복숭아 한번 더 추가
remove(PyBag, '자두') # 자두 삭제
print("가방속의 물건: ", PyBag)
print("가방 속 과일 수: " , count(PyBag))
print("복숭아 개수: ", numOf(PyBag, '복숭아'), '\n')  # 리스트 pyBag에 있는 '복숭아'의 개수 조사

remove(PyBag, '복숭아')    # '복숭아' 삭제
print("가방속의 물건: ", PyBag)
# 가방속의 물건:  ['사과', '파인애플', '배', '복숭아']
# 리스트의 원소를 삭제 시, 만약 리스트에 같은 값의 원소(여기서는 '복숭아')가 있다면 
# 가장 앞에 있는 원소부터 삭제된다.
print("복숭아가 있나요? " , contains(PyBag, '복숭아'), '\n')  # 가장 뒤에 하나 남아있음

remove(PyBag, '복숭아')    # '복숭아' 삭제
print("가방속의 물건: ", PyBag)
# 가방속의 물건:  ['사과', '파인애플', '배']
print("복숭아가 있나요? " , contains(PyBag, '복숭아'), '\n')  # '복숭아' 없음

