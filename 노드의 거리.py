from collections import deque

# 큐 만들어야하니까 데크 넣고

T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):  # 테스트 케이스 돌면서

    V, E = map(int, input().split())

    # V는 노드갯수
    # E는 간선 정보

    # 주어진 출발 노드에서 최소 몇 개의 간선을 지나면 도착 노드에 갈 수 있나?

    # E개 줄에 걸쳐, 간선의 양쪽 노드 번호 주어짐
    # 2차원 배열 만들라는 소리겠지요

    graph = [[] for _ in range(V + 1)]  # E개 줄짜리에 간선 양쪽 노드 번호 붙은 그래프 생성

    # 얘는 인접 리스트라고 한다 저장 몬함
    for _ in range(E):
        a, b = map(int, input().split())
        graph[a].append(b)  # a에서 b로 갈 수 있다
        graph[b].append(a)  # 무방향이라 양방향으로 쳐박음 (b에서 a로 갈 수 있다는 뜻)

    S, G = map(int, input().split())


    # 시작 S
    # 도착 G

    def bfs(graph, S, G):  # 넓이 우선 탐색 할 함수 만들기

        visited = [0] * (V + 1)  # 방문한거 흔적 남겨둘 배열 만들기

        q = deque()  # 어디로 갈건지 저장해둘 큐 만들고
        q.append(S)  # 일단 시작점을 큐에 집어넣고 시작
        visited[S] = 1  # 그리고 시작점에 갔다고 1로 표시함 (나중에 길이 계산으로도 씀)

        while q:  # 큐에 뭐가 남아있는 한 계속 돌면서
            now = q.popleft()  # 지금 어디여

            # 그리고 그 팝한거 근처에 붙어서 갈 수 있는걸 뒤져봐야지 (대충 인접노드 찾으라는 소리임)

            if now == G:  # 지금 장소가 도착지라면
                return visited[now] - 1  # 시작을 1로 했으니까 -1 해서 거리 반환

            else:
                for nxt in graph[now]:  # 지금 있는 노드랑 붙어있는 놈들 뒤져서
                    if visited[nxt] == 0:  # 아직 방문 안 했으면
                        q.append(nxt)
                        visited[nxt] = visited[now] + 1  # 이만큼 갔다 하고 거리 +1이나 해줌
        return 0  # 뱉을건 따로 없음;;

    print(f"#{test_case} {bfs(graph,S, G)}")
