MAX_QSIZE = 20

class CircularQueue:
  def __init__(self):               # 생성자  
    self.front = 0                  # 큐의 전단 위치
    self.rear = 0                   # 큐의 후단 위치
    self.items = [None] * MAX_QSIZE # 항목 저장용 리스트

  def isEmpty(self): return self.front == self.rear
  def isFull(self): return self.front == (self.rear + 1) % MAX_QSIZE
  def clear(self): self.front = self.rear

  def enqueue(self,item):
    if not self.isFull():                       # 꽉 차있지 않을 시
      self.rear = (self.rear + 1) % MAX_QSIZE   # rear 회전
      self.items[self.rear] = item              # rear 위치에 삽입

  def dequeue(self):                            
    if not self.isEmpty():                      # 비어있지 않을 시
      self.front = (self.front + 1) % MAX_QSIZE # front 회전
      return self.items[self.front]             # front위치의 item 반환

  def peek(self):
    if not self.isEmpty():                              # 비어있지 않을 시
      return self.items[(self.front + 1) % MAX_QSIZE]   # front 다음에 있는 위치의 아이템을 반환

  def size(self):                                             
    return (self.rear - self.front + MAX_QSIZE) % MAX_QSIZE    # 원형 큐의 사이즈 반환

  def display(self):
    out = []
    if self.front < self.rear:
      out = self.items[self.front + 1 : self.rear + 1]
    else:
      out = self.items[self.front + 1 : MAX_QSIZE] \
        + self.items[0:self.rear + 1]
    print("[f=%s,r=%d] ==> "%(self.front, self.rear),out)


class TNode:                                # 이진트리를 위한 노드 클래스
    def __init__(self, data, left = None, right = None):  # 생성자
        self.data = data                    # 노드의 데이터
        self.left = left                    # 왼쪽 자식을 위한 링크
        self.right = right                  # 오른쪽 자식을 위한 링크



def preorder(n):        # 전위 순회 함수
    if n is not None:
        print(n.data, end='')       # 먼저 루트노드 처리(화면 출력)
        preorder(n.left)            # 왼쪽 서브트리 처리
        preorder(n.right)           # 오른쪽 서브트리 처리

def inorder(n):         # 중위 순회 함수
    if n is not None:
        inorder(n.left)             # 왼쪽 서브트리 처리
        print(n.data, end='')       # 루트노드 처리(화면 출력)
        inorder(n.right)           # 오른쪽 서브트리 처리

def postorder(n):       # 후위 순회 함수
    if n is not None:
        postorder(n.left)            # 왼쪽 서브트리 처리
        postorder(n.right)           # 오른쪽 서브트리 처리
        print(n.data, end='')        # 루트노드 처리(화면 출력)

def levelorder(root):
    queue = CircularQueue()         # 큐 객체 초기화
    queue.enqueue(root)             # 최초에 큐에는 루트 노드만 들어있음
    while not queue.isEmpty():      # 큐가 공백상태가 아닌동안,
        n = queue.dequeue()         # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data,end='')    # 먼저 노드의 정보를 출력
            queue.enqueue(n.left)   # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)  # n의 오른쪽 자식 노드를 큐에 삽입

def count_node(n):      # 순환을 이용해 트리의 노드 수를 계산하는 함수
    if n is None:   # n이 None이면 공백 트리 --> 0을 반환
        return 0
    else:               # 좌우 서브트리의 노드수의 합 + 1을 반환 (순환 이용)
        return 1 + count_node(n.left) + count_node(n.right)

def count_leaf(n):
    if n is None:                               # 공백트리 --> 0을 반환
        return 0
    elif n.left is None and n.right is None:    # 단말노드 --> 1을 반환
        return 1
    else:                                       # 비단말 노드: 좌우 서브트리의 결과 합을 반환
        return count_leaf(n.left) + count_leaf(n.right)

def calc_height(n):
    if n is None:                   # 공백트리 --> 0을 반환
        return 0
    hLeft = calc_height(n.left)     # 왼쪽 트리의 높이 --> hLeft
    hRight = calc_height(n.right)   # 오른쪽 트리의 높이 --> hRight
    if(hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1

def path_length(root,lv = 1):   # 루트부터 모든 자식 노드까지의 경로의 길이의 합
    n = root
    left = 0
    right = 0
    if n is not None:           # 비어있지 않을 시
        if n.left != None:      # 왼쪽 자식노드가 비어있지 않다면
            left = lv           # 왼쪽 자식노드까지의 경로 길이를 저장
        if n.right != None:     # 오른쪽 자식노드가 비어있지 않다면
            right = lv          # 오른쪽 자식노드까지의 경로 길이를 저장
        return left + right + path_length(n.left,lv+1) + path_length(n.right,lv+1)  
        # 현재 노드에서 자식노드까지의 길이 + 자식노드에서 다음 노드의 길이들
    else:
        return 0

def reverse(root):
    if(root != None):
        q = CircularQueue()
        q.enqueue(root)         # 큐에 root 삽입
        while not q.isEmpty():  # 큐가 비어있지 않을 때는 반복
            n = q.dequeue()     # 가장 앞 큐 원소 추출
            if not(n.left is None and n.right is None):     # 단말이 아닐 때 
                tmp = n.left
                n.left = n.right
                n.right = tmp
                # 왼쪽과 오른쪽을 바꿈
                if n.left is not None:  # 왼쪽 자식노드가 비어있지 않다면
                    q.enqueue(n.left)   # 큐 원소로 추가
                if n.right is not None: # 오른쪽 자식노드가 비어있지 않다면
                    q.enqueue(n.right)  # 큐 원소로 추가

def BinaryTree1():
    g = TNode('G')
    h = TNode('H')
    e = TNode('E', g, h)
    d = TNode('D')
    f = TNode('F')
    b = TNode('B', d)
    c = TNode('C', e, f)
    root = TNode('A', b, c)

    print('\n <BinaryTree1>     # (P8.1)',end='')
    print('\n전위 순회 : ', end='')
    inorder(root)
    print('\n중위 순회 : ', end='')
    preorder(root)
    print('\n후위 순회 : ', end='')
    postorder(root)
    print('\n레벨 순회 : ', end='')
    levelorder(root)

    print()
    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 단말의 개수 = %d개" % count_leaf(root))
    print(" 트리의 높이 = %d" % calc_height(root))

def BinaryTree2():
    a = TNode('A')
    b = TNode('B')
    slash = TNode('/', a, b)
    c = TNode('C')
    star1 = TNode('*', slash, c)
    d = TNode('D')
    star2 = TNode('*', star1, d)
    e = TNode('E')
    root = TNode('+', star2, e)

    print('\n <BinaryTree2>     # (P8.1)',end='')
    print('\n전위 순회 : ', end='')
    inorder(root)
    print('\n중위 순회 : ', end='')
    preorder(root)
    print('\n후위 순회 : ', end='')
    postorder(root)
    print('\n레벨 순회 : ', end='')
    levelorder(root)

    print()
    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 단말의 개수 = %d개" % count_leaf(root))
    print(" 트리의 높이 = %d" % calc_height(root))

def BinaryTree3():
    c = TNode('C')
    d = TNode('D')
    f = TNode('F')
    b = TNode('B', c, d)
    e = TNode('E', None, f)
    root = TNode('A', b, e)

    print('\n <BinaryTree3>     # (P8.5 ~ P8.6)',end='')
    print('\n전위 순회 : ', end='')
    inorder(root)
    print('\n중위 순회 : ', end='')
    preorder(root)
    print('\n후위 순회 : ', end='')
    postorder(root)
    print('\n레벨 순회 : ', end='')
    levelorder(root)
    reverse(root)
    print('\n---좌우 대칭 후---',end='')
    print('\n전위 순회 : ', end='')
    inorder(root)
    print('\n중위 순회 : ', end='')
    preorder(root)
    print('\n후위 순회 : ', end='')
    postorder(root)
    print('\n레벨 순회 : ', end='')
    levelorder(root)


    print()
    print(" 노드의 개수 = %d개" % count_node(root))
    print(" 단말의 개수 = %d개" % count_leaf(root))
    print(" 트리의 높이 = %d" % calc_height(root))
    print('경로 길이의 합 : ',end='')
    print(path_length(root),'\n')
    


print('  === LinkedBinaryTree ===')
BinaryTree1()
BinaryTree2()
BinaryTree3()
