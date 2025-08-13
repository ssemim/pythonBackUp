T = int(input())  # 테스트케이스 받고

for test_case in range(1, T + 1):
    N = int(input())  # 파스칼 삼각형의 크기


    # 삼각형 크기 만큼 돌면서, 크기가 1증가할 때 마다 하나씩 출력 개수가 늘고
    # 파스칼의 삼각형에서
    # 삼각형 행의 처음과 끝은 무조건 1이다
    # 삼각형 N번째 행의 둘째 자리는 무조건 N-1이다
    # 또 뭐있냐 이거 어떡하냐

    stack = []

    for i in range(N+1):  # 삼각형 크기만큼 반복하는데
        if i == 0 or i == N: # 첫 행은 항상 1
            stack.append(1)
        elif i == 1 or i == N-1: # 둘째행은 항상 N-1
            stack.append(N-1)
        else :
            for j in range(N): #점화식 어케세워 사람살려 (n-1)C(r-1) 이거 어케하냐고 여기서



    print(*stack)