class Bag:
    bag = []

    def __init__(self):
    # 파이썬 클래스 생성자
        pass

    def insert(self,e):
        self.bag.append(e)
    # 클래스 Bag에 성분 e를 추가하는 메소드

    def remove(self,e):
        self.bag.remove(e)
     # 클래스 Bag에 성분 e를 제거하는 메소드

    def count(self):
        return len(self.bag)
     # 클래스 Bag의 성분 개수를 반환하는 메소드
    
    def contains(self,e):
        return e in self.bag
     # 클래스 Bag에 성분 e의 유무를 판단한 뒤, True or False로 반환하는 메소드

    def numOf(self,e):
        n = 0
        for s in self.bag :  # 리스트 bag의 성분들을 모두 조사하여
            if s == e:
                n = n + 1
        # item과 일치할 시, n의 카운트 1 증가
        return n
     # 클래스 Bag에 e와 일치하는 리스트 원소의 개수를 반환하는 메소드

myBag = Bag()
myBag.insert('휴대폰')
myBag.insert('지갑')
myBag.insert('손수건')
myBag.insert('빗')
myBag.insert('자료구조')
myBag.insert('야구공')
print('내 가방속의 물건:',myBag.bag)

myBag.insert('빗')
myBag.remove('손수건')
print('내 가방속의 물건:',myBag.bag)
print('가방 안 물건 개수:',myBag.count())
print('가방 안에 있는 빗 개수:',myBag.numOf('빗'))
print('가방 안에 축구공이 있습니까?', myBag.contains('축구공'))


