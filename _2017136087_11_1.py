INF= 9999
def choose_vertex(dist, found):         # 최소 dist 정점을 찾는 함수
    min = INF
    minpos = -1
    for i in range(len(dist)):          # 모든 정점 중에서
        if dist[i] < min and found[i] == False:
            min = dist[i]
            minpos = i
    return minpos                       # 최소 dist정점의 인덱스 반환

def shortest_path_dijkstra(vtx, adj, start):
    vsize = len(vtx)                                # 정점 수
    dist = list(adj[start])                         # dist 배열 생성 및 초기화
    path = [start] * vsize                          # path 배열 생성 및 초기화
    found = [False] * vsize                         # found 배열 생성 및 초기화
    found[start] = True                             # 시작정점: 이미 찾아짐
    dist[start] = 0                                 # 시작정점의 거리 0


    for i in range(vsize):
        u = choose_vertex(dist, found)              # 최소 dist 정점 u 탐색
        found[u] = True                             # u는 이제 찾아짐

        for w in range(vsize):                      # 모든 정점에 대해
            if not found[w]:                        # 아직 찾아지지 않았으면
                if dist[u] + adj[u][w] < dist[w]:   # 갱신 조건 검사 
                    dist[w] = dist[u] + adj[u][w]   # dist 갱신
                    path[w] = u                     # 이전 정점 갱신
                    
    return path, dist                               # 찾아진 최단 경로와 거리 반환

vertex = ['A', 'B', 'C', 'D', 'E', 'F', 'G']
weight = [[0,   7,   INF, INF, 3,   10,  INF],
          [7,   0,   4,   10,  2,   6,   INF],
          [INF, 4,   0,   2,   INF, INF, INF],
          [INF, 10,  2,   0,   11,  9,   4  ],
          [3,   2,   INF, 11,  0,   INF,  5  ],
          [10,  6,   INF, 9,   INF,  0,   INF],
          [INF, INF, INF, 4,   5,   INF, 0  ]]


start = 0       # 시작 정점은 0번, 'A'로 선택
cnt = 1         # 카운트 변수
path, dist = shortest_path_dijkstra(vertex, weight, start)  # 최종 경로를 출력하기 위한 코드
print("Src->DST       Dist    Path")
for end in range(len(vertex)):
    pathlist = []           # 리스트 초기화
    if end != start:        # end 가 start가 아닐 시
        print(" %s -> %s\t\t"%(vertex[start], vertex[end]), end='')
        pathlist.append(vertex[end])            # 가장 먼저 도착지점 추가
        while(path[end] != start):              # 경로의 end가 start일 때까지 반복
            pathlist.append(vertex[path[end]])  # 경로리스트에 이전 경로 정점을 추가
            end = path[end]                     # end는 이전 경로의 정점이 됨
        pathlist.append(vertex[path[end]])      # 결과적으로 마지막 end는 start가 나오게 됨 => pathlist에 추가
        print("%2d     "%dist[cnt],end='')      # dist를 처음부터 하나씩 출력
        cnt += 1                                # 카운트 변수
        pathlist = list(reversed(pathlist))     # pathlist는 거꾸로 되어있는 상태이기에 뒤집어줌
        for i in range(len(pathlist)):
            print("%s"%pathlist[i],end=' ')     # 경로 출력
        print()