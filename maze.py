T = int(input())


# si, sj : 시작점 좌표
def DFS(si, sj):
    # 중복체크 배열도 2차원
    visited = [[0] * N for _ in range(N)]
    # (x,y)를 탐색한적이 있다 => visited[x][y] = 1
    # (w,z)를 탐색한적이 없다 => visited[w][z] = 0

    stack = []

    # 현재 탐색중인 위치
    vi, vj = si, sj

    # 시작지점 방문 체크
    visited[vi][vj] = 1

    # 델타배열
    di = [-1, 1, 0, 0]
    dj = [0, 0, -1, 1]

    # 탐색 시작
    while True:

        # 현재 위치 디버깅용
        # for i in range(N):
        #     for j in range(N):
        #         if (i,j) == (vi,vj):
        #             print("*",end="")
        #         else:
        #             print(maze[i][j],end="")
        #     print()
        # print("==================")

        # print(vi,vj)
        # 현재 위치 (vi,vj) 에서 탐색
        # 현재 위치가 도착점인가? 검사
        if maze[vi][vj] == 3:
            # 도착점 왔으면 더이상 진행할 필요 없음
            return 1
        # (vi,vj)에서 갈 수 있는 다른 위치 찾기
        # (ni,nj) : 다른 위치
        # 4방향
        for d in range(4):
            # d 방향으로 갔을때 다른 위치 ni nj 구하기
            ni = vi + di[d]
            nj = vj + dj[d]

            # 1. (ni,nj)가 2차원배열 범위 안인지
            # 2. 실제로 갈수 있다라고 표시된 곳인지(벽==1 or 길==0)
            # 3. 이전에 방문한적 없는지
            if ((0 <= ni < N and 0 <= nj < N) and
                    (maze[ni][nj] != 1) and
                    (not visited[ni][nj])):
                # print("이동")
                # (ni,nj)로 이동할것이기 떄문에 현재 위치(vi,vj)를 스택에 저장
                stack.append((vi, vj))
                visited[ni][nj] = 1
                vi, vj = ni, nj
                break
        # for-else
        else:
            # 중간에 break를 한적이 없다=> 갈수있는 방향이 없다.
            # 길이 없다는 거니까 돌아가자.
            # 어디로돌아가는데? 스택이 알고있다.
            if stack:
                vi, vj = stack.pop()
            else:
                break

    # 탐색을 다 마쳤는데 3을 발견 못하면 return 0
    return 0


def DFS2(si, sj): # 이건 파이썬 내장 함수 호출 스택안에 다 맡기고 튀는거임 (직접 안만들어도 되도록)
    # 재귀로 함 해보자
    # 현재 위치 si,sj 방문체크

    visited2[si][sj] = 1

    # 재귀 호출 종료 (도착지점을 찾음)

    if maze[si][sj] == 3:
        return 1
    else:
        # 못찾았다면 다른 위치로 이동
        # 방향마다 한번씩 재귀호출 해 줘야함

        for di, dj in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
            ni, nj = si + di, sj + dj
            if 0 <= ni < N and 0 <= nj < N and maze[ni][nj] != 1 and not visited[ni][nj]:
                DFS2(ni, nj)

            return 1

        else:
            return 0


for tc in range(1, T + 1):
    # 미로의 크기
    N = int(input())

    # 미로
    maze = [list(map(int, input())) for _ in range(N)]

    # 탐색 시작 좌표
    # si, sj
    for i in range(N):
        for j in range(N):
            if maze[i][j] == 2:
                # 시작점
                si, sj = i, j

    print(f"#{tc} {DFS(si, sj)}")

"""
1
5
13101
10101
10101
10101
10021



3
5
13101
10101
10101
10101
10021
5
10031
10111
10101
10101
12001
5
00013
01110
21000
01111
00000

"""
