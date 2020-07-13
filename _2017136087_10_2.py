# 10.6 브릿지 확인
def dfs_cc(vertex, adjMat, color, val, visited):    # 연결되어 있는 정점 모두 색칠하는 함수
    if val not in visited:
        visited.add(val)
        color.append(val)
        s = vertex.index(val)                   # start의 인접 배열 인덱스 찾기
        n = 0
        for i in range(0,len(adjMat[s])):       # start의 인접 배열 검사
            if adjMat[s][n] == 1:               # 인접 정점에 해당된다면 
                dfs_cc(vertex, adjMat, color, vertex[n], visited) # 이 인접정점에 dfs 시행
            n += 1                              # 대상을 다음 원소로
    return color

def find_connected_component(vertex, adjMat):               # 연결 구성 요소 찾기(여기서는 개수 반환)
    visited = set()
    colorList = []

    for vtx in vertex:
        if vtx not in visited:                              # 방문하지 않은 정점이라면
            color = dfs_cc(vertex, adjMat,[],vtx,visited)   # 방문 후 
            colorList.append(color)                         # 방문한 정점들을 새로 등록
    return len(colorList)                                   # 연결 구성 요소 개수 반환
    
def findBridge(vertex, adjMat):                             # 브릿지 찾기 함수
    num = find_connected_component(vertex, adjMat)          # 기존 그래프의 연결 구성 요소 개수 저장
    for i in range(0,len(vertex)):                          # 모든 요소를 한번씩 짝지어서 확인
        for j in range(i+1,len(vertex)):
            if adjMat[i][j] == 1 or adjMat[j][i] == 1:      # 연결되어 있다면
                adjMat[i][j] = 0                            # 연결을 끊음
                adjMat[j][i] = 0
                if find_connected_component(vertex, adjMat) > num :     # 연결 구성 요소가 더 많아졌다면
                    print("(%c , %c) "%(vertex[i], vertex[j]),end='')   # 브릿지라는 것이기 때문에 출력
                adjMat[i][j] = 1                            # 원상복구
                adjMat[j][i] = 1


            
vertex = ['A', 'B', 'C', 'D', 'E', 'F']
adjMat = [[0, 1, 0, 1, 0, 0,],
          [1, 0, 1, 1, 1, 0,],
          [0, 1, 0, 0, 0, 1,],
          [1, 1, 0, 0, 1, 0,],
          [0, 1, 0, 1, 0, 0,],
          [0, 0, 1, 0, 0, 0,]]

print("Bridge: ",end='')
findBridge(vertex, adjMat)
print()