from collections import deque

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서
    N, M = map(int, input().split())
    # N개의 숫자로 이루어진 수열
    # M번 맨 뒤로 보내는 작업
    # 수열의 맨 앞에 있는 숫자를 출력하는 법은?
    dq = deque()

    numbers = list(map(int, input().split())) # 숫자 받아오고

    for i in range(N):# 받은 숫자 떄려넣어서 데크 만들거
        dq.append(numbers[i])

    for i in range(M):
        dq.append(dq.popleft())  # 맨 앞 빼서 맨 뒤로 보냄

    print(f'#{test_case} {dq[0]}')
