def dfs(row, current_sum):
    global min_sum   # 함수 안에서 전역 변수 min_sum을 수정하기 위해 global 선언


    if current_sum >= min_sum: # 가지치기: 지금까지의 합이 이미 최소합보다 크거나 또이또이시 더 볼 필요 없긔
        return

    if row == N: # 모든 행(N행)을 다 돌았다면 최소합 덮어쓰기
        min_sum = current_sum
        return


    for col in range(N): # 현재 행(row)에서 고를 수 있는 열(col)들을 하나씩 골라보자
        if not visited[col]:   # 아직 사용하지 않은 열이라면
            visited[col] = True   # 해당 열 사용 체크
            dfs(row + 1, current_sum + arr[row][col])   # 다음 행으로 넘어가며 합계 추가
            visited[col] = False  # 탐색 전체 다 끝나면 이제 다시 써도 됨이라고 체크


T = int(input())   # 테스트 케이스 개수 입력
for tc in range(1, T + 1):
    N = int(input())   # 배열 크기 N 입력
    arr = [list(map(int, input().split())) for _ in range(N)]   # NxN 배열 입력

    visited = [False] * N   # 각 열의 사용 여부를 체크하는 리스트
    min_sum = float('inf')  # 최소합을 저장할 변수 (처음에는 ㅈㄴ 큰수필요해서 무한대라고 함)

    dfs(0, 0)   # 0행부터, 합계는 0으로 시작
    print(f"#{tc} {min_sum}")
