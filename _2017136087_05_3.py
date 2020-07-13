import math
MAZE_SIZE = 10  # 미로의 크기
(ox,oy) = (9,8)

class SortedPriorityQueue:
  def __init__(self):
    self.items = [] # items리스트에는 (x,y,-d)와 같은 튜플 형식의 데이터가 들어감

  def isEmpty(self):
    return len(self.items) == 0
  def size(self): return len(self.items)
  def clear(self): self.items = []

  def findMaxIndex(self):    # 가장 큰 우선순위의 인덱스 찾기
    if self.isEmpty(): return None
    else:
      highest = 0
      for i in range(1,self.size()):
        if self.items[i][2] > self.items[highest][2]:   # items의 ?번째에 있는 요소2 => 거리
                                                        # 즉, 거리를 기준으로 우선순위 결정
          highest = i       # 최고 우선순위 인덱스 갱신
      return highest

  def enqueue(self,item):   # 삽입 연산(정렬)
    self.items.append(item)
    self.items = sorted(self.items, key=lambda items: items[2]) # 2번째 요소(거리)를 기준으로 정렬
                                                                # lambda는 함수를 축소해서 식으로 만들기 위한 기능

  def dequeue(self):        # 삭제 연산 - 우선순위 정렬을 통해 O(n) -> O(1) 
    if not self.isEmpty():
      return self.items.pop(self.size()-1)

  def peek(self):           # peek 연산 - 우선순위 정렬을 통해 O(n) -> O(1)
   if not self.isEmpty():
      return self.items[self.size()-1]  # 꺼내지 않고 반환

def isValidPos(x,y):
  if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
    return False
  else:
    return map[y][x] == '0' or map[y][x] == 'x'

def dist(x,y):
  (dx,dy)= (ox-x, oy-y)
  return math.sqrt(dx*dx + dy*dy)

def SpecialSearch():          # 최소거리 전략의 미로탐색
  q = SortedPriorityQueue()   # 우선순위 큐 객체 생성
  q.enqueue((0,2,-dist(0,2)))   # 튜플에 거리정보 추가
  print('SortedPQueue: ')

  while not q.isEmpty():
    here = q.dequeue()
    print(here[0:2], end=' -> ')    # (x,y,-d)에서 (x,y)만 출력
    x,y,_ = here                    # (x,y,-d)에서->(x,y,_)
    if map[y][x] == 'x': return True
    else:
      map[y][x] = '.'
      if isValidPos(x,y-1): q.enqueue((x,y-1,-dist(x,y-1)))
      if isValidPos(x,y+1): q.enqueue((x,y+1,-dist(x,y+1)))
      if isValidPos(x-1,y): q.enqueue((x-1,y,-dist(x-1,y)))
      if isValidPos(x+1,y): q.enqueue((x+1,y,-dist(x+1,y)))
    print('우선순위큐: ', q.items)
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
result = SpecialSearch()
if result: print("미로탐색 성공!")
else: print("미로탐색 실패...")
    


