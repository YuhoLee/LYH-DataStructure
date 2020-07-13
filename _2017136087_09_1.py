class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None


def search_bst(n, key):                 # 이진탐색트리 탐색연산(순환)
    if n == None:
        return None
    elif key == n.key:                  # n의 키 값과 동일->탐색성공
        return n
    elif key < n.key:                   # key<n의 키
        return search_bst(n.left,key)   # 순환호출로 왼쪽 서브트리 탐색
    else:                               # key>n의 키
        return search_bst(n.right, key) # 순환호출로 오른쪽 서브트리 탐색


def search_value_bst(n,value):          # 이진탐색트리 탐색연산(preorder사용): 값을 이용한 탐색
    if n == None: return None
    elif value == n.value:              # n의 value와 동일->탐색성공
        return n
    res = search_value_bst(n.left, value)   # 왼쪽 서브트리에서 탐색
    if res is not None:                     # 탐색이 성공하면
        return res                          # 결과 반환
    else:                                   # 왼쪽에서 탐색 실패이면
        return search_value_bst(n.right, value) # 오른쪽을 탐색해 결과 반환


def search_max_bst(n):                      # 최대 값의 노드 탐색
    while n != None and n.right != None:    
        n = n.right
    return n


def search_min_bst(n):                      # 최소 값의 노드 탐색
    while n != None and n.left != None:
        n = n.left
    return n


def insert_bst(r, n):            # 이진탐색트리 삽입연산 (노드를 삽입함): 순환구조 이용
    if n.key < r.key:                       # 삽입할 노드의 키가 루트보다 작으면
        if r.left is None:                  # 루트의 왼쪽 자식이 없으면
            r.left = n                      # n은 루트의 왼쪽 자식이 됨
            return True
        else:                               # 루트의 왼쪽 자식이 있으면
            return insert_bst(r.left, n)    # 왼쪽 자식에게 삽입하도록 함
    elif n.key > r.key:                     # 삽입할 노드의 키가 루트보다 크면
        if r.right is None:                 # 루트의 오른쪽 자식이 없으면
            r.right = n                     # n은 루트의 오른쪽 자식이 됨
            return True
        else:                               # 루트의 오른쪽 자식이 있으면
            return insert_bst(r.right, n)   # 오른쪽 자식에게 삽입하도록 함
    else:                                   # 키가 중복되면
        return False                        # 삽입하지 않음


def delete_bst_case1(parent, node, root):
    if parent is None:              # 삭제 할 단말 노드가 루트이면
        root = None                 # 공백 트리가 됨
    else:
        if parent.left == node:     # 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None      # 부모의 왼쪽 링크를 None
        else:                       # 오른쪽 자식이면
            parent.right = None     # 부모의 오른쪽 링크를 None

    return root                     # root가 변경될 수도 있으므로 반환


def delete_bst_case2(parent, node, root):
    if node.left is not None:           # 삭제 할 노드가 왼쪽 자식만 가짐
        child = node.left               # child는 왼쪽 자식
    else:                               # 삭제할 노드가 오른쪽 자식만 가짐
        child = node.right              # child는 오른쪽 자식

    if node == root:                    # 없애려는 노드가 누트이면
        root = child                    # 이제 child가 새로운 루트가 됨
    else:
        if node is parent.left:         # 삭제할 노드가 부모의 왼쪽 자식
            parent.left = child         # 부모의 왼쪽 링크를 변경
        else:                           # 삭제할 노드가 부모의 오른쪽 자식
            parent.right = child        # 부모의 오른쪽 링크를 변경

    return root                         # root가 변경될 수도 있으므로 반환


def delete_bst_case3(parent, node, root):
    succp = node                    # 후계자의 부모 노드
    succ = node.right               # 후계자 노드
    while (succ.left != None):      # 후계자와 부모노드 탐색
        succp = succ
        succ = succ.left       

    if(succp.left == succ):         # 후계자가 왼쪽 자식이면
        succp.left = succ.right     # 후계자의 오른쪽 자식 연결
    else:                           # 후계자가 오른쪽 자식이면
        succp.right = succ.right    # 후계자의 왼쪽 자식 연결

    node.key = succ.key             # 후계자의 키와 값을
    node.value = succ.value         # 삭제할 노드에 복사
    node = succ                     # 실제로 삭제하는 것은 후계자 노드

    return root                     # 일관성을 위해 root반환


def delete_bst(root, key):                  # 이진탐색트리 삭제연산 (노드를 삭제함)
    if root == None: return None            # 공백 트리

    parent = None                           # 삭제 할 노드의 부모 탐색
    node =  root                            # 삭제할 노드 탐색
    while node != None and node.key != key: # parent 탐색
        parent = node
        if key < node.key : node = node.left
        else: node = node.right

    if node == None: return None                    # 삭제할 노드가 없음
    if node.left == None and node.right == None:    # case 1: 단말 노드
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:   # case 2: 유일한 자식
        root = delete_bst_case2(parent, node, root)
    else:                                           # case 3: 두 개의 자식
        root = delete_bst_case3(parent, node, root)
    return root                                     # 변경된 루트 노드를 반환


# 9.1
def search_max_bst_rec(n):                      # 최대 값의 노드 탐색(순환)
    if n is not None:                           # 입력 노드가 비어있지 않을 때
        if n.right is None:                     # 오른쪽 자식이 비어있다면
            return n                            # 해당 노드 키 반환
        else:                                   # 비어있지 않다면
            return search_max_bst_rec(n.right)  # 오른쪽 자식에 대한 재귀 호출
    return None                                 # 입력 노드가 비어있을 시 None 반환


def search_min_bst_rec(n):                      # 최소 값의 노드 탐색(순환)
    if n is not None:                           # 입력 노드가 비어있지 않을 때
        if n.left is None:                      # 왼쪽 자식이 비어있다면
            return n                            # 해당 노드 키 반환
        else:                                   # 비어있지 않다면
            return search_min_bst_rec(n.left)   # 왼쪽 자식에 대한 재귀 호출
    return None                                 # 입력 노드가 비어있을 시 None 반환


#9.2
def insert_bst_iter(r, n):                      # 이진탐색트리 삽입연산 (노드를 삽입함): 반복구조 이용
    while r is not None:                        # 루트 노드가 None이 아닐 때까지
        if n.key < r.key:                       # 삽입할 노드의 키가 루트보다 작으면
            if r.left is None:                  # 루트의 왼쪽 자식이 없으면
                r.left = n                      # n은 루트의 왼쪽 자식이 됨
                return True
            else: r = r.left                    # 루트의 왼쪽 자식 노드를 루트로 설정
        elif n.key > r.key:                     # 삽입할 노드의 키가 루트보다 크면
            if r.right is None:                 # 루트의 오른쪽 자식이 없으면
                r.right = n                     # n은 루트의 오른쪽 자식이 됨
                return True
            else: r = r.right                   # 루트의 오른쪽 자식 노드를 루트로 설정
        else: return False                      # 키가 중복되면 삽입하지 않음
    return False



