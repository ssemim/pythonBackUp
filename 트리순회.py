"""
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
"""
# 트리 노드의 수
N = int(input())
# 트리 정보 => 두개씩 끊어서 읽으면 앞쪽이 부모번호, 뒤쪽이 자식번호
tree = list(map(int, input().split()))

# 부모 노드 번호를 인덱스로 사용하는 방법
cleft = [0] * (N + 1)
cright = [0] * (N + 1)

for i in range(N - 1):
    # 앞이 부모
    p = tree[i * 2]
    # 뒤가 자식
    c = tree[i * 2 + 1]

    # p번 노드의 왼쪽 자식이 없다면
    if cleft[p] == 0:
        # c번 노드를 p번 노드의 왼쪽 자식으로
        cleft[p] = c
    else:
        # 왼쪽 자식이 있다면 오른쪽 자식으로
        cright[p] = c

print(cleft)
print(cright)


# 서브트리로 쪼개고 나서
# 루트 : V
# 왼쪽 SUB : L
# 오른쪽 SUB : R

# 1. 전위 순회 : V - L - R
def preorder(t):
    # t번 노드가 존재하는 노드면 순회
    if t:
        # V 노드에서 해야할 연산 코드 작성
        print(t, end=" ")
        # L : t번 노드의 왼쪽을 전위순회
        preorder(cleft[t]) # 왼쪽자식 노드 있으면 출격
        # R : t번 노드의 오른쪽을 전위순회
        preorder(cright[t])


print("====전위 순회====")
preorder(1)


# 2. 중위 순회 : L - V - R
def inorder(t):
    # t번 노드가 존재하는 노드면 순회
    if t:

        # L : t번 노드의 왼쪽을 중위순회
        inorder(cleft[t])
        # V 노드에서 해야할 연산 코드 작성
        print(t, end=" ")
        # R : t번 노드의 오른쪽을 중위순회
        inorder(cright[t])


print(" \n====중위 순회====")
inorder(1)


# 3. 후위 순회 : L - R - V
def postorder(t):
    # t번 노드가 존재하는 노드면 순회
    if t:
        # L : t번 노드의 왼쪽을 후위순회
        postorder(cleft[t])
        # R : t번 노드의 오른쪽을 후위순회
        postorder(cright[t])
        # V 노드에서 해야할 연산 코드 작성
        print(t, end=" ")


print(" \n====후위 순회====")
postorder(1)

print()
