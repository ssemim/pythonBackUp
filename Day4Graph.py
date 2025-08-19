T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T+1):
    V, E = map(int, input().split())
    # V와 E : V는 노드 E는 간선
    adjL = []
    # 출발 도착 노드 간선 정보 받을 배열
    for getNode in range(1,E+1):


