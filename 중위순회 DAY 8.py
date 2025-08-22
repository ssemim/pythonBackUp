def inorder(v):
    if v:
        inorder(left[v])     # 왼쪽 자식
        print(node[v], end="")  # 자기 자신 (문자 출력)
        inorder(right[v])    # 오른쪽 자식


for tc in range(1, 11):  # 테스트 케이스 10개
    N = int(input())     # 정점 개수
    node = [""] * (N + 1)
    left = [0] * (N + 1)
    right = [0] * (N + 1)

    for _ in range(N):
        info = input().split()
        idx = int(info[0])   # 정점 번호
        node[idx] = info[1]  # 문자 저장
        if len(info) >= 3:
            left[idx] = int(info[2])
        if len(info) == 4:
            right[idx] = int(info[3])

    print(f"#{tc} ", end="")
    inorder(1)   # 루트(1)부터 중위 순회 시작
    print()
