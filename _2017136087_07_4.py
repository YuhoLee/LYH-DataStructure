class Entry:
    def __init__(self,key,value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s"%(self.key, self.value))


class LinearProbMap:    
    def __init__(self,M):
        self.table = [None]*M       # 크기 M인 테이블을 먼저 만듦
        self.M = M
        print("리스트 크기:",self.M)

    def hashFn(self,key):       # 사용 할 해시 함수 
        sum = 0
        for c in key:               # 문자열의 모든 문자에 
            sum = sum + ord(c)      # 아스키 코드 값을 모두 더함
        return sum % self.M

    def insert(self, key, value):       # (key,value) 입력
        idx = self.hashFn(key)          # 해시 주소 계산
        step = idx
        while True:     # 계속 반복
            if self.table[step] == None or self.table[step] == True:    # 해당 주소가 비어있으면
                self.table[step] = Entry(key,value)   # 엔트리 추가
                print("삽입:", self.table[step])            # 메세지 출력
                break
            else:
                step += 1        # 다음 주소로 이동
                if step == self.M:    # 리스트의 끝이라면
                    step = 0     # 리스트의 처음으로
                if step == idx:    # 전부 돌아서 idx가 원래대로 돌아오면
                    print("삽입: Can't insert (FULL)")    # 꽉찼다는 메세지
                    return  

    def search(self,key):               # 검색
        idx = self.hashFn(key)  
        step = idx
        while self.table[step] is not None:
            if self.table[step] == True:        # 저장되었다가 삭제된 공간일 시
                step += 1                       # 다음 주소로 이동
            elif self.table[step].key != key:   # key가 일치하지 않을 시
                step += 1                       # 다음 주소로 이동
            else:                               # key가 일치할 시
                return self.table[step]         # 엔트리 반환
            if step == self.M:    # 리스트의 끝이라면
                step = 0     # 리스트의 처음으로
            if step == idx:    # 전부 돌아서 idx가 원래대로 돌아오면
                return None    # 찾기 실패
        return None     # 탐색 오류

    def delete(self, key):
        res = self.search(key)              # search 활용
        if res is not None:                 # 탐색 성공 시
            s = self.table.index(res)       # 만들었던 search를 활용하여 삭제 할 자리를 찾은 후 
            self.table[s] = True            # 삭제 시, None과 구별해주기 위해 True를 사용
        print("삭제:",res)                  # 메세지 출력
                
    def display(self,msg):
        print(msg)
        for s in range(len(self.table)):
            if self.table[s] != None and self.table[s] != True:     # 리스트가 비어있지 않을 시
                idx = self.hashFn(self.table[s].key)
                print("[%2d] -> "%s,end='')
                print(self.table[s],end='')
                print("  /  해시 주소: %d"%idx)

map = LinearProbMap(4)            # 맵 객체 생성
map.insert('data','자료')       # 맵에 엔트리를 삽입
map.insert('structure','구조')
map.insert('HashChainMap','해시 연결 맵')
map.insert('game','게임')
map.insert('binary search','이진 탐색')
map.display("\n나의 단어장:")     # 맵 출력
print()

print("탐색: game -->", map.search('game'))
print("탐색: over -->", map.search('over'))
print("탐색: data -->", map.search('data'))
print("탐색: hang -->", map.search('hang'))
print()

map.delete('game')
map.delete('code')
map.display("\n나의 단어장:")
print()

