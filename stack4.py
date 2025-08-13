T = 10  # 테스트케이스 받고

for test_case in range(1, T + 1):
    NM = list(map(str, input().split()))

    N = int(NM[0])  # N은 문자열의 총 수
    M = NM[1]  # M은 받은 문자열
    arr = list(M.strip())  # 받은 문자열을 리스트로

    top = -1  # 탑 기초 셋팅
    stack = [''] * 100  # 스택으로 쓸 배열 셋팅

    for arg in arr:
        if top >= 0 and arg == stack[top]:  # 새로 들어온 숫자가 같은 숫자면 pop
            top -= 1
        else:
            top += 1  # 아니면 push
            stack[top] = arg

    print(f'# {test_case} {"".join(stack[:top+1])}')
