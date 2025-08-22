"""
1. 부모 노드 번호를 인덱스로 사용해서 자식 노드 번호를 저장하는 방법
4
1 2 1 3 3 4 3 5

"""

# 간선의 개수
E = int(input())
N = 5
# 트리 노드 정보 한줄로 입력
tree = list(map(int, input().split()))

#

left_child = [0] * (N + 1)  # 왼쪽 자식 저장할 배열
# left_child[i] = i번 노드의 왼쪽 자식 노드번호
right_child = [0] * (N + 1)  # 오른쪽 자식 저장할 배열
# right_child[i] = i번 노드의 오른쪽 자식 노드 번호

for i in range(4):
    # 자식을 넣을때는 => 자식이 아예 없으면 왼쪽 먼저
    # 넣으려고 했는데 왼쪽 자식이 없으면 오른쪽 자식이 된다
    p = tree[i * 2]  # 부모 노드 번호
    c = tree[i * 2 + 1]  # 자식 노드 번호

    # p번 노드의 왼쪽 자식이 없으면 c를 p의 왼쪽 자식으로
    if left_child[p] == 0:
        left_child[p] = c
    # 왼쪽 자식이 있으면 c를 p의 오른쪽 자식으로
    else:
        right_child[p] = c

print("부모 번호 :", *list(range(N + 1)))
print("======================")
print("왼쪽 자식 번호 : ", *left_child)
print("오른쪽 자식 번호 : ", *right_child)
