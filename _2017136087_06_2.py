class Node():   # 노드 클래스
    def __init__(self, elem, link):
        self.data = elem
        self.link = link

class LinkedList:       # 연결리스트 클래스
    def __init__(self):
        self.head = None

    def isEmpty(self):  # 비어있는지 확인
        return self.head == None

    def push(self, item):   # 앞에서 추가
        self.head = Node(item, self.head)

    def pop(self):      # 앞에서 빼내기
        if not self.isEmpty():
            data = self.head.data
            self.head = self.head.link
            return data

    def peek(self):     # head가 가리키는 항목 데이터 반환
        if not self.isEmpty():
            return self.head.data

    def display(self, msg = 'LinkedList:'):     # 연결리스트 출력
        print(msg, end='')
        node = self.head
        while not node == None:
            print(node.data, end=' ')
            node = node.link
        print()

    def size(self):     # 연결리스트 크기 반환
        node = self.head
        count = 0
        while not node == None:
            node = node.link
            count += 1
        return count

    def getNode(self,pos):      # pos번째 노드 반환
        if pos < 0: return None
        node = self.head
        while pos > 0 and node != None:
            node = node.link
            pos -= 1
        return node

    def getEntry(self,pos):     # pos번째 노드의 데이터 반환
        node = self.getNode(pos)
        if node == None : return None
        else: return node.data

    def replace(self,pos,elem):
        node = self.getNode(pos)
        if node != None: node.data = elem

    def find(self,data):    # 같은 데이터 찾기
        node = self.head
        while node is not None:
            if node.data == data: return node
            node = node.link
        return None

    def insert(self,pos,elem):      # pos에 노드 삽입
        before = self.getNode(pos-1)
        if before == None:
            self.head = Node(elem,self.head)
        else:
            before.link = Node(elem,before.link)

    def delete(self,pos):       # pos에 있는 노드 삭제
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link

class Term:     # 계수와 지수 클래스
    def __init__(self, expo, coef):
        self.expo = expo
        self.coef = coef

class SparsePoly(LinkedList):   # 희소 다항식 클래스
    def __init__(self):
        super().__init__()
        self.expo = 0
        self.coef = 0

    def read(self):     # 사용자 입력 함수
        while True:
            try:    # EOF 예외처리
                coef,expo = input("계수 차수 입력(종료:ctrl + z): ").split()     # 입력받은 값을 공백 기준으로 분리
                self.coef = float(coef)
                self.expo = int(expo)
                # 입력 시, 연결리스트의 가장 뒤에 추가되도록 함.
                if self.head == None:
                    self.head = Node(Term(self.expo,self.coef),None)
                    node = self.head
                else:
                    node.link = Node(Term(self.expo,self.coef),None)
                    node = node.link
            except EOFError:    # EOF 입력 시 반복문 탈출
                break
        print("\t입력 다항식: ", end = '')
        self.display()
        
    def display(self,s=''):     # 희소 다항식 출력
        print(s,end='')
        for i in range(0,self.size()):
            print("  +%.1lf X^%d"%(self.getEntry(i).coef, self.getEntry(i).expo), end = '')
        print()

    def add(self,polyB):    # 다항식의 합
        polyC = SparsePoly()    # 반환 할 희소 다항식 객체
        list = []
        nA = self.head
        nB = polyB.head
        # 두 다항식에 노드가 있는동안 반복수행
        while nA != None and nB != None: 
            # 다항식 A의 지수가 다항식 B의 지수와 같은 경우
            if nA.data.expo == nB.data.expo:
                # nA의 계수 + nB의 계수
                sum = nA.data.coef + nB.data.coef
                list.append(Term(nA.data.expo,sum))
                nA = nA.link
                nB = nB.link
            # 다항식 A의 지수가 다항식 B의 지수보다 큰 경우
            elif nA.data.expo > nB.data.expo:
                list.append(Term(nA.data.expo,nA.data.coef))
                nA = nA.link
            # 다항식 A의 지수가 다항식 B의 지수보다 작은 경우
            else:
                list.append(Term(nB.data.expo,nB.data.coef))
                nB = nB.link
        # nA가 None 아닐 때 까지 push 수행
        while nA != None:
            list.append(Term(nA.data.expo,nA.data.coef))
            nA = nA.link
        # nB가 None 아닐 때 까지 push 수행
        while nB != None:
            list.append(Term(nB.data.expo,nB.data.coef))
            nB = nB.link

        # 리스트에 추가한 데이터를 거꾸로 연결리스트에 추가시킴
        # 리스트에 추가한 이유는 그냥 연결리스트에 추가하게 되면 
        # 큰 수부터 추가되기 때문에 작은 수부터 추가하기 위함이다.
        for i in range(len(list)-1,-1,-1):
            polyC.push(list[i])
        return polyC


a = SparsePoly()
b = SparsePoly()
a.read()
b.read()
c = a.add(b)
a.display("\t A = ")
b.display("\t B = ")
c.display("\tA+B= ")


        




