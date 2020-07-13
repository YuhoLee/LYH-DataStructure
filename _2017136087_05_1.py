import queue
MAZE_SIZE = 10  # 미로의 크기

def isValidPos(x,y):
  if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE:
    return False
  else:
    return map[y][x] == '0' or map[y][x] == 'x'
    
def DFS():  # 깊이 우선탐색 함수
  Q = queue.LifoQueue(maxsize=20) # Lifo Queue -> Stack
  Q.put((0,2))  # 시작 위치
  cnt = 0   # 출력을 한눈에 하기 위한 카운트변수
  print('DFS: ')

  while not Q.empty():  # 스택이 비어있지 않을 시
    here = Q.get()  # 항목을 꺼냄
    print(here, end=' -> ')
    cnt = (cnt + 1) % 5
    if cnt == 0: print()
    (x,y) = here  # 스택에 저장되어 있는 튜플은 (x,y) 순서임
    if map[y][x] == 'x':  # 출구일 시
      return True   # 탐색 성공
    else:
      map[y][x] = '.' # 지나온 곳을 표시함
      # 4방향의 이웃을 검사하여 갈 수 있는 곳이면 스택에 삽입
      if isValidPos(x,y-1): Q.put((x,y-1)) # 상
      if isValidPos(x,y+1): Q.put((x,y+1)) # 하
      if isValidPos(x-1,y): Q.put((x-1,y)) # 좌
      if isValidPos(x+1,y): Q.put((x+1,y)) # 우

  return False      # 스택이 비어있기에 탐색 실패


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

result = DFS()
if result: print("미로탐색 성공!")
else: print("미로탐색 실패...")


