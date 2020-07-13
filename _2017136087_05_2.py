MAX_QSIZE = 10                      # 원형 큐 크기
MAZE_SIZE = 10                      # 미로의 크기

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

def isValidPos(x,y):  # 지나갈 수 있는 곳인지 확인하는 함수
  if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
    return False
  else:
    return map[y][x] == '0' or map[y][x] == 'x'   # 지나갈 수 있는 곳 or 도착 지점

def BFS():
  que = CircularQueue()
  que.enqueue((0,2))
  cnt = 0   # 출력을 한눈에 하기 위한 카운트변수
  print('BFS: ')

  while not que.isEmpty():
    here = que.dequeue()
    print(here,end = ' -> ')
    cnt = (cnt + 1) % 5
    if cnt == 0: print()  # 길게 쭉 출력되지 않도록 하기 위함
    x,y = here
    if map[y][x] == 'x': return True
    else:
      map[y][x] = '.'
      if isValidPos(x,y-1) : que.enqueue((x,y-1))   # 상
      if isValidPos(x,y+1) : que.enqueue((x,y+1))   # 하
      if isValidPos(x-1,y) : que.enqueue((x-1,y))   # 좌
      if isValidPos(x+1,y) : que.enqueue((x+1,y))   # 우
  return False


map = [['1','1','1','1','1','1','1','1','1','1'],
       ['1','1','1','1','0','0','0','0','1','1'],
       ['e','0','1','1','1','0','1','0','0','1'],
       ['1','0','0','0','1','0','1','1','0','0'],
       ['1','0','1','0','0','0','0','1','1','1'],
       ['1','0','0','1','1','1','0','0','1','1'],
       ['1','0','1','1','0','0','1','0','0','1'],
       ['0','0','0','0','0','1','1','0','1','1'],
       ['1','1','1','1','0','1','0','0','0','x'],
       ['1','1','1','1','1','1','1','1','1','1']]

result = BFS()
if result: print("미로탐색 성공!")
else: print("미로탐색 실패...")

