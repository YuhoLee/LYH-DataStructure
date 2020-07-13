# 10.1 인접행렬 깊이우선탐색, 10.2 인접행렬 너비우선탐색

import collections              # 덱 클래스 collection.deque 사용 가능
import collections as cols      # collections.deque 대신 cols.deque 사용

def dfs(vertex, adjMat, start, visited = set()):   # 처음 호출할 때 visited 공집합
    if start not in visited :                   # start가 방문하지 않은 정점이면
        visited.add(start)                      # start를 방문한 노드 집합에 추가
        print(start, end=' ')                    # start를 방문했다고 출력함
        s = vertex.index(start)                 # start의 인접 배열 인덱스 찾기
        n = 0
        for i in range(0,len(adjMat[s])):       # start의 인접 배열 검사
            if adjMat[s][n] == 1:               # 인접 정점에 해당된다면 
                dfs(vertex, adjMat, vertex[n], visited) # 이 인접정점에 dfs 시행
            n += 1                              # 대상을 다음 원소로

def bfs(vertex, adjMat, start):  
    visited = set([start])              # 맨 처음은 start만 방문한 정점
    queue = cols.deque([start])         # 컬렉션의 덱 객체 생성(큐로 사용)
    while queue:                        # 공백이 아닐 때까지
        val = queue.popleft()           # 큐에서 하나의 정점 val를 빼냄
        print(val, end=' ')             # val 방문했음을 출력
        s = vertex.index(val)           # 빼낸 정점의 인접 배열 인덱스 찾기
        n = 0
        for i in range(0,len(adjMat[s])):              
            if adjMat[s][n] == 1 and vertex[n] not in visited:
                visited.add(vertex[n])              # 이제 v는 방문했음
                queue.append(vertex[n])             # v를 큐에 삽입
            n += 1                                  # 대상을 다음 원소로


vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
adjMat = [[0, 1, 1, 0, 0, 0, 0, 0],
          [1, 0, 0, 1, 0, 0, 0, 0],
          [1, 0, 0, 1, 1, 0, 0, 0],
          [0, 1, 1, 0, 0, 1, 0, 0],
          [0, 0, 1, 0, 0, 0, 1, 1],
          [0, 0, 0, 1, 0, 0, 0, 0],
          [0, 0, 0, 0, 1, 0, 0, 1],
          [0, 0, 0, 0, 1, 0, 1, 0]]

print("DFS: ",end='')
dfs(vertex, adjMat, 'A')
print()
print("BFS: ",end='')
bfs(vertex, adjMat, 'A')
print()
