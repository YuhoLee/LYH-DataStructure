class Stack:
    def __init__(self):
        self.top = []

    def isEmpty(self): return len(self.top) == 0
    def size(self): return len(self.top)
    def clear(self): self.top = []

    def push(self,item):
        self.top.append(item)

    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]

def isValidSource( srcfile ):
    s = Stack()
    i = 0
    j = 0
    for line in srcfile :
        i += 1
        for token in line:
            j += 1
            if token in "{[(":
                s.push(token)
            elif token in "}])":
                if s.isEmpty() :
                    return "Error: 2", i, j         # 조건2 위반
                else:
                    left = s.pop()
                    if(token == "}" and left != "{") or \
                      (token == "]" and left != "[") or \
                      (token == ")" and left != "(") :
                        return "Error: 3", i, j     # 조건3 위반
    if not s.isEmpty():
        return "Error: 1", i, j                     # False이면 조건1 위반
    else:
        return 0, i, j


#filename = "ArrayStack.h"
#filename = "CheckBracketMain.cpp"
print("\t [ 파일 괄호 검사 ]\t\n")
filename = input("괄호 검사를 할 파일 이름을 입력해주세요: ")

infile = open(filename , "r")
lines = infile.readlines();
infile.close()

print(lines)
eCode, lcnt, ccnt = isValidSource(lines)
print(filename, " ---> ", eCode)
print(" 라인수 = ", lcnt)
print(" 문자수 = ", ccnt)



