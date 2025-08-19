T = 10  # 테스트케이스 개수

for _ in range(T):

    tc_num, E = map(int, input().split())  # 테스트 케이스랑 간선 갯수 받고

    # 인접 행렬 초기화 (100x100 전부 0)
    adj = [[0] * 100 for _ in range(100)]

    edges = list(map(int, input().split()))  # 간선 정보 입력받아 인접 행렬에 기록
    for i in range(0, len(edges), 2):
        u = edges[i]  # 출발 정점
        v = edges[i + 1]  # 도착 정점
        adj[u][v] = 1  # 길 있음 표시

    # DFS 준비
    visited = [0] * 100  # 방문 체크 배열
    stack = [0]  # 시작점 0에서 출발
    visited[0] = 1 # 출발점은 이미 출발했으니 1로 바꿈

    found = 0  # 99에 도달 여부 표시

    while stack: # DFS 고고
        cur = stack.pop()  # 현재 정점

        if cur == 99:  # 목적지 도착
            found = 1
            break

        # 현재 정점에서 갈 수 있는 모든 정점 확인
        for nxt in range(100):
            if adj[cur][nxt] == 1 and visited[nxt] == 0:
                stack.append(nxt)
                visited[nxt] = 1

    # 결과 출력
    print(f"#{tc_num} {found}")
