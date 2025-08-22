"""
2. 자식 노드 번호를 인덱스로 사용해서 부모 노드 번호를 저장하는 방법
4
1 2 1 3 3 4 3 5

"""
# 간선의 개수
E = int(input())
N = 5
# 트리 노드 정보 한줄로 입력
tree = list(map(int, input().split()))

for i in range(E):
    c = tree[i * 2]  # 자식 노드 번호
    p = tree[i * 2 + 1]  # 부모 노드 번호

# 5번 노드의 조상 노드 모두 찾기
child = 5

ancestor = []

while parent[child] != 0:
    # 부모 노드가 0이 나오면 루트 노드라는 뜻
    # 원래 child의 부모 노드의 부모 노드를 알아내기 위해 바꿔주기

    child = parent[child]
    ancestor.append(child)

root = child
print(root,ancestor)
