class Polynomial:
    def __init__(self): # 생성자
        self.coef = []  # 다항식의 계수들이 모여있는 리스트

    def degree(self):   # 최고차항의 계수를 반환하는 메소드
        return len(self.coef) - 1   # 리스트 전체 크기 - 1
 
    def display(self, msg = "f(x) = "): # 입력한 값에 따른 다항식 생성
        print(msg,end ='')
        for i in range(len(self.coef)-1,-1,-1): # 리스트 coef를 거꾸로 반복
            if(self.coef[i] != 0):  # 0이 아닐 시, 해당 차수를 출력하도록 함
                print(" + %.1lf x^%d"%(self.coef[i],i),end='')    
        print()

    def evaluate(self, scalar): # scalar를 받으면 다항식의 x에 scalar를 대입하여 연산하는 메소드
        val = 0
        for i in range(len(self.coef)-1,-1,-1): # 리스트 coef를 거꾸로 반복
            val += self.coef[i] * scalar ** i
        return  val

    def add(self, rhs): # 두 다항식을 더하는 메소드
        val = Polynomial()
        a = len(self.coef)
        b = len(rhs.coef)
        if a > b:   # 불러온 객체 리스트 크기가 더 크면
            for i in range(b):
                val.coef.append(0)
                val.coef[i] = self.coef[i] + rhs.coef[i]
            # 인수로 받은 객체 리스트 크기까지만 서로 리스트를 더하여 추가하고
            for i in range(b,a):
                val.coef.append(0)
                val.coef[i] = self.coef[i]
            # 불러온 객체 리스트의 남은 차수(더 높은 차수의 계수)의 리스트 원소들을 추가해줌

        else:   # 인수로 받은 객체 리스트 크기가 더 크거나 같으면
            for i in range(a):
                val.coef.append(0)
                val.coef[i] = self.coef[i] + rhs.coef[i]
            # 불러온 객체 리스트 크기까지만 서로 리스트를 더하여 추가하고
            for i in range(a,b):
                val.coef.append(0)
                val.coef[i] = rhs.coef[i]
            # 인수로 받은 객체 리스트의 남은 차수(더 높은 차수의 계수)의 리스트 원소들을 추가해줌
        return val
            
    def subtract(self, rhs): # 두 다항식을 빼는 메소드
        val = Polynomial()
        a = len(self.coef)
        b = len(rhs.coef)
        if a > b:   # 불러온 객체 리스트 크기가 더 크면
            for i in range(b):
                val.coef.append(0)
                val.coef[i] = self.coef[i] - rhs.coef[i]
            # 인수로 받은 객체 리스트 크기까지만 서로 리스트를 빼서 추가하고
            for i in range(b,a):
                val.coef.append(0)
                val.coef[i] = self.coef[i]
            # 불러온 객체 리스트의 남은 차수(더 높은 차수의 계수)의 리스트 원소들을 추가해줌

        else:   # 인수로 받은 객체 리스트 크기가 더 크거나 같으면
            for i in range(a):
                val.coef.append(0)
                val.coef[i] = self.coef[i] - rhs.coef[i]
            # 불러온 객체 리스트 크기까지만 서로 리스트를 빼서 추가하고
            for i in range(a,b):
                val.coef.append(0)
                val.coef[i] = -rhs.coef[i]
            # 인수로 받은 객체 리스트의 남은 차수(더 높은 차수의 계수)의 리스트 원소들에 -를 달아서 추가해줌
        return val

    def multiply(self,rhs): # 해당 메소드를 불러온 객체와 인수로 받은 객체의 리스트를 빼는 메소드# 두 다항식을 곱하는 메소드 
        val = Polynomial()
        a = len(self.coef)
        b = len(rhs.coef)
        for i in range((a-1)*(b-1)):    # 두 다항식을 곱했을 때의 최고차항의만큼 리스트 공간을 만들어 준 뒤
            val.coef.append(0)
        for i in range(a):
            for j in range(b):
                val.coef[i+j] += self.coef[i] * rhs.coef[j] 
        return val

def read_poly():    # 입력을 받아 다항식을 만드는 함수 (클래스 내부 메소드 아님!)
    p = Polynomial()
    deg = int(input("다항식의 최고 차수를 입력하시오: "))
    for n in range(deg+1):  # 최고차항의 계수부터 순서대로 x^0의 계수까지 입력받도록 함
        coef = float(input(  "\tx^%d의 계수: "%(deg-n)))
        p.coef.append(coef) # 객체 p의 coef리스트에 입력하였던 계수coef를 추가
    p.coef.reverse()    # 리스트의 index와 해당차수를 맞추도록 리스트를 역순으로 뒤집음
    return p


a = read_poly()
b = read_poly()
print()

print("\n*add, subtract, multiply 테스트")
c = a.add(b)
d = a.subtract(b)
e = a.multiply(b)
a.display("\tA(x) = ")
b.display("\tB(x) = ")
c.display("\tC(x) = ")
d.display("\tD(x) = ")
e.display("\tE(x) = ")
print("\n*degree, evaluate 테스트\n")
print("A(x)의 최고차항 = ",a.degree())
print("B(x)의 최고차항 = ",b.degree())
print("C(x)의 최고차항 = ",c.degree())
print("D(x)의 최고차항 = ",d.degree())
print("E(x)의 최고차항 = ",e.degree())
print("A(2) = ",a.evaluate(2))
print("B(2) = ",b.evaluate(2))
print("C(2) = ",c.evaluate(2))
print("D(2) = ",d.evaluate(2))
print("E(2) = ",e.evaluate(2))