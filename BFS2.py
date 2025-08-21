from collections import deque

# 2차원 배열에서는 인접한 정점 => 상하좌우
di = [-1, 1, 0, 0]
dj = [0, 0, -1, 1]

N = 7
maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 1, 1, 1, 1, 1, 0],
        [0, 1, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 0, 0],
        [1, 0, 1, 1, 1, 0, 1],
        [1, 0, 1, 99, 0, 0, 0],
        [0, 0, 1, 1, 1, 0, 1]]

maze = [[0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0]]


def where_am_i(i, j, visited):
    for ni in range(N):
        for nj in range(N):
            if (i, j) == (ni, nj):
                print("★", end=" ")
            else:
                print(visited[ni][nj], end=" ")
        print()
    print("=================")


def is_valid(i, j):
    return 0 <= i < N and 0 <= j < N


# si , sj : 시작 위치 좌표(si : 행번호, sj : 열번호)
def bfs(si, sj):
    # 중복체크
    visited = [[0] * N for _ in range(N)]
    # 큐 생성
    q = deque()
    # 시작 위치 큐에 넣고
    q.append((si, sj))

    # 큐안에 탐색할 좌표가 남아있으면 계속
    while q:
        # 큐에서 다음 탐색 위치 꺼내오기
        i, j = q.popleft()

        where_am_i(i,j,visited)

        # 이 꺼낸 위치(내가 방문하고 있는 위치) 도착점인지 판단
        if maze[i][j] == 99:
            print(f"탈출 : ({i},{j}), 거리 : {visited[i][j]}")
            return visited[i][j]  # 거리 반환

        # 이 i,j 와 인접한 상하좌우 방향 확인
        # 상하좌우에 방문할 곳이 있는지 판단
        for d in range(4):
            # 상하좌우로 1칸씩 이동한 좌표 계산
            ni = i + di[d]
            nj = j + dj[d]
            # 이동후 좌표가 ni, nj 방문 가능한 위치인가?
            # 1. ni, nj 가 유효한 인덱스 범위 안
            # 2. 방문한 적이 없어야한다.
            # 3. maze[ni][nj] != 1 : 벽(1)이 아니여야 이동 가능
            if is_valid(ni, nj) and not visited[ni][nj] and maze[ni][nj] != 1:
                # 위의 3개의 조건을 만족하면 ni, nj 는 방문 가능한 위치
                # 큐에 다음에 방문할 것이다. 라고 예약
                q.append((ni, nj))
                # 중복방지 + 거리계산
                visited[ni][nj] = visited[i][j] + 1

    # while 문 종료 후 코드가 여기까지 실행 되엇다
    # 중간에 우리가 찾는 목표 지점을 찾지 못했다.
    print("실패")
    return -1


bfs(3, 3)
