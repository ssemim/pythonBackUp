T = int(input())  # 테스트케이스 받고

for test_case in range(1, 1 + T):
    txt = list(map(str, input().strip()))

    top = -1
    stack = [''] * 1000

    for arg in txt:
        if top >= 0 and arg == stack[top]:  # 같은 문자면 pop
            top -= 1
        else:
            top += 1  # 같은 문자 아니면 푸시
            stack[top] = arg

    print(f'#{test_case} {top + 1}')
