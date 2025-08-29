T = 10  # 10개의 테스트 케이스고

for test_case in range(1, 11):  # 10개의 테스트 케이스 돌면서
    # 테스트 케이스 첫줄 => 정점 N
    N = int(input())

    # 그다음 N 줄에 걸쳐 각 정점의 정보가 주어진다.

    # 정점이 정수면 정점 번호와 양의 정수가 주어지고,
    # 정점이 연산자이면
    # 정점 번호, 연산자, 해당 정점의 왼쪽 자식, 오른쪽 자식의 정점 번호가
    # 차례대로 주어진다.

    # 그러니까 정수인지 아닌지 판단해서 정수가 맞으면 그 자리에 띨롱 집어넣고
    # 정수 아니면 (연산자면) 그 밑에 새끼 친거 왼쪽 오른쪽 집어넣으면 된단거지

    # 연산을 하려면 자식 노드 (연산자 아닌거) 값이 먼저 필요하니까
    # 후위순회를 하자 (그러면 연산자인 V가 제일 늦게 나옴)

    tree = [0] * (N + 1)  # 트리 저장할 배열 생성

    for _ in range(N):  # 정점의 개수만큼 반복하면서 노드 정보 넣고
        parts = input().split()  # 입력 일단 공백 기준으로 나눠서 받고
        node = int(parts[0])  # 첫 번째는 정점 번호
        if parts[1] in '+-*/':  # 두 번째가 연산자면 연산자 노드
            op = parts[1]  # 연산자 중 하나
            left = int(parts[2])  # 왼쪽 자식 노드 번호
            right = int(parts[3])  # 오른쪽 자식 노드 번호
            tree[node] = (op, left, right)  # 배열에 저장함 (튜플임 이거 여러개라서)
        else:  # 숫자 노드일 경우
            tree[node] = int(parts[1])  # 정수 값으로 저장


    def post_order(node):

        if type(tree[node]) == int:  # 숫자 노드면
            return tree[node]
        else:  # 나머지는 연산자
            op, left, right = tree[node]
            left_val = post_order(left) # 왼쪽 자식 재귀로 꺼내서 계산
            right_val = post_order(right) # 오른쪽 자식도 재귀로 꺼내서 계산
            if op == '+':  # 덧셈
                return left_val + right_val
            elif op == '-':  # 뺄셈
                return left_val - right_val
            elif op == '*':  # 곱셈
                return left_val * right_val
            elif op == '/':  # 나눗셈
                return left_val // right_val


    result = post_order(1)

    print(f'#{test_case} {result}')
