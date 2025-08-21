# 달팽이는 1부터 N*N까지의 숫자가 시계방향으로 이루어짐
# 달팽이 크기 N은 1이상 10이하의 정수

# 가장 첫 줄에는 테스트 케이스 개수 T가 주어지고, 그 아래로 각 테스트 케이스가 주어짐
# 각 테스트 케이스에는 N이 주어짐

# 각 줄은 #t로 시작, 빈 칸을 사이에 두고 달팽이 숫자를 출력

T = int(input())

for test_case in range(1, T + 1):
    N = int(input())

    # N은 달팽이 사이즈
    # 달팽이 숫자 넣을 배열 만들자

    snail = [[0] * N for _ in range(N)]

    # N*N의 배열 생성 완

    # 자 그럼 돌아가면서 숫자 채우자
    # 달팽이 껍데기 시계방향으로 움직이니까 델타 써보자

    # 오른쪽, 아래, 왼쪽, 위
    di = [0, 1, 0, -1]
    dj = [1, 0, -1, 0]

    i, j, d = 0, 0, 0  # 시작 위치와 방향
    for num in range(1, N * N + 1):
        snail[i][j] = num
        ni, nj = i + di[d], j + dj[d]

        # 다음 칸이 범위 밖이거나 이미 채워졌으면 방향 전환
        if not (0 <= ni < N and 0 <= nj < N and snail[ni][nj] == 0):
            d = (d + 1) % 4
            ni, nj = i + di[d], j + dj[d]

        i, j = ni, nj

    print(f"#{test_case}")
    for row in snail:
        print(" ".join(map(str, row)))
