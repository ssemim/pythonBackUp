from collections import deque

# 큐 쓸거니까 또 데크 집어넣고

T = 10  # 테스트 케이스 10개라고 함

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    testNum = int(input())  # 젤 처음 주는 번호가 테스트 케이스 넘버임

    # 16 x 16 행렬이고
    # 0 이 길
    # 1 이 벽
    # 2 가 시작점
    # 3 이 도착점

    graph = []  # 받을 그래프 미리 만들어놓고
    for _ in range(16):  # 한줄씩 받아넣어서 16X16 2차원 행렬을 만듬
        row = list(map(int, input().strip()))
        graph.append(row)

    for i in range(16):
        for j in range(16):  # 2차원 배열 돌면서 시작점 도착점 뽑아내자
            if graph[i][j] == 2:
                si, sj = i, j
            if graph[i][j] == 3:
                ei, ej = i, j

    # si , sj : 시작 위치 좌표(si : 행번호, sj : 열번호)
    def bfs(si, sj):
        # 방문했는지 체크 할 배열 생성 (이것도 2차원임 그래프 따라서)
        visited = [[0] * 16 for _ in range(16)]
        # 큐 생성
        q = deque()
        # 시작 위치 큐에 넣고
        q.append((si, sj))

        # 이동할 좌표 찍어 상하좌우 무빙쳐야지 (델타 쓰자 와)
        di = [-1, 1, 0, 0]
        dj = [0, 0, -1, 1]

        # 큐안에 탐색할 좌표가 남아있으면 계속 돌면서
        while q:
            # 큐에서 다음 탐색 위치 꺼내오기
            i, j = q.popleft()

            if graph[i][j] == 3:  # 도착지 도착! 1반환
                return 1

            else:  # 도착지 아니면
                for d in range(4):  # 상하좌우 무빙치면서
                    ni, nj = i + di[d], j + dj[d]

                    # 범위 안에 있고, 벽이 아니고, 방문 안했으면 갈수있슴
                    if 0 <= ni < 16 and 0 <= nj < 16 and graph[ni][nj] != 1 and not visited[ni][nj]:
                        visited[ni][nj] = 1
                        q.append((ni, nj))  # 간곳 1로 만들고 다시 큐에 넣어 다음 무빙 준비

        return 0  # 큐 다 돌고 도착 못했으면 실패

    print(f"#{test_case} {bfs(si, sj)}")
