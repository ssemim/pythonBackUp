# 전위 순회 하도록 연결리스트로 코드 만들어 보아라

class Node:
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


A = Node("A")
B = Node("B")
C = Node("C")

A.left = B
A.right = C


def preorder(node):
    # t번 노드가 존재하는 노드면 순회
    if node:

        print(node.value, end=" ")  # V 노드에서 해야할 연산 코드 작성
        preorder(node.left)  # L 노드에서 해야할 연산 코드 작성
        preorder(node.right)  # R 노드에서 해야할 연산 코드 작성


print("===전위 순회===")
print(f'{preorder(A)}')
