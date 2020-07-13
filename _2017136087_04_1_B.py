# 보너스문제를 통해 바꾼 코드
class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0    # 비었을 시 False반환
    def size(self): return len(self.top)    # 스택 크기 반환
    def clear(self): self.top = []  # 스택 비우기

    def push(self,item):    
        self.top.append(item)   # 스택에 아이템 추가

    def pop(self):
        if not self.isEmpty():      # 비어있지 않다면
            return self.top.pop(-1) # 가장 나중에 들어온 원소를 스택에서 빼고 반환

    def peek(self):
        if not self.isEmpty():      # 비어있지 않다면
            return self.top[-1]     # 가장 나중에 들어온 원소 반환

def checkChar(token):
    global Qflag 
    global qflag 
    global Mflag
    # 전역에서 선언한 Qflag, qflag, Mflag를 가져옴
    if token == "'" or token == '"' or Mflag != True:
    # 주석이 아닌 상태에서 따옴표를 만났을 때
        if token == "'" and Qflag == False:
        # 작은따옴표 만났을 때/끝날 때
            qflag = not qflag   # 작은 따옴표 활성화 / 종료 
        if token == '"' and qflag == False:
        # 큰따옴표 만났을 때/끝날때
            Qflag = not Qflag 
        return True
    if Qflag == True or qflag == True :
    # 따옴표가 열려있을 때
        return True
    if token == '#' and (Qflag != True or qflag != True):
    # 따옴표가 아닌 상태에서 주석을 만났을 때
        Mflag = not Mflag   # 주석 활성화
        return True
    if Mflag == True:   
    # 주석이 활성화 되어있을 때 
        return True
    return False

def isValidSource( srcfile ):
    s = Stack()
    i = 0   # 줄 카운트
    j = 0   # 문자 수 카운트
    global Mflag    # '전역에서 선언한 Mflog를 가져옴
    for line in srcfile :
        i += 1
        Mflag = False   # 주석 초기화
        for token in line:
            j += 1
            if checkChar(token):    # True 반환 시 continue
                continue
            if token in "{[(":  # 왼쪽 괄호 만났을 때
                s.push(token)
            elif token in "}])":    # 오른쪽 괄호 만났을 때
                if s.isEmpty() :    # 스택이 비어있다면
                    return "Error: 2", i, j         # 조건2 위반
                else:
                    left = s.pop()  # 가장 나중에 들어온 스택 원소 추출 
                    if(token == "}" and left != "{") or \
                      (token == "]" and left != "[") or \
                      (token == ")" and left != "(") :
                    # 같은 종류의 괄호가 아니라면
                        return "Error: 3", i, j     # 조건3 위반
    if not s.isEmpty():                             
       # 비어있지 않다면
        return "Error: 1", i, j                     # 조건1 위반
    else:
        return 0, i, j


Qflag = False
qflag = False
Mflag = False
# flag 전역변수

#filename = "ArrayStack.h"
#filename = "CheckBracketMain.cpp"
print("\t [ 파일 괄호 검사 ]\t\n")
filename = input("괄호 검사를 할 파일 이름을 입력해주세요: ")

infile = open(filename , "r")   # 파일 열기
lines = infile.readlines()      # 파일 라인단위로 읽어들여 리스트 저장
infile.close()                  # 파일 닫기

eCode, lcnt, ccnt = isValidSource(lines)    # 파일 검사
print(filename, " ---> ", eCode)
print(" 라인수 = ", lcnt)
print(" 문자수 = ", ccnt)



