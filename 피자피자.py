from collections import deque

# 피자피자피자피자

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    N, M = map(int, input().split())  # N과 M 받아오기
    # N = 화덕크기
    # M = 피자 개수

    cheese = list(map(int, input().split()))  # 배열로 피자 치즈 양 받아오고

    waiting = deque()

    for i in range(M):
        waiting.append((i + 1, cheese[i]))   # 튜플로 번호와 치즈 같이 저장
    # 굽기전 놈이라 웨이팅이라고 할래 피자 대기용 데크

    # 여기서 순서대로 뽑아서 오븐에 넣을거임
    # 화덕 크기가 N개이므로 M개 중에 N개를 먼저 굽는다.
    # 그리고 자리가 날 때 마다 그 다음 인덱스의 피자를 넣는당 (맛있겠다)

    oven = deque()  # 얘도 그 뭐냐 피자 굽는용 데크

    # 피자 대기열에 있는거 뽑아서 오븐에 넣음
    # 화덕 크기는 N!
    # 화덕이 한 바퀴 돌 때 마다 치즈가 반씩 녹으므로
    # for문 돌면서, 자기 차례가 됐을 때, if 문으로 치즈 다녹았나 보고
    # 다 녹았으면 OK 합격 pop / 새거 넣고
    # 덜 녹았으면 ㄴㄴ 기다려 뒷순번으로 다시 넣어줌 (한바퀴 더돌려서 또확인해)

    for i in range(N):
        oven.append(waiting.popleft())   # 그대로 꺼내서 넣으면 됨

        # 일단 처음에 오븐에 피자 넣음

        # 여기까지 하면 피자 N개 다 넣은거고 1번 자리 피자가 꺼낼 수 있게 돌아옴

    baking = True  # 오븐구워지는즁

    while baking:  # 오븐에 마지막거 남아있기 전까지 반복
        if len(oven) == 1:
            baking = False
        else:
            oven_number, now_pizza = oven.popleft()  # 번호, 치즈양 꺼냄
            now_pizza //= 2  # 치즈 녹임

            if now_pizza > 0:  # 아직 ㄴ
                oven.append((oven_number, now_pizza))
            else:  # 다 녹음 굿
                if waiting:
                    oven.append(waiting.popleft())  # 새 피자 투입
                else:
                    pass  # 넣을거 없으니 패스

    print(f'#{test_case} {oven[0][0]}')
