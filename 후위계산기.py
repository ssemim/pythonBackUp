# 후위 표기식을 계산하려면 스택을 이용해야 함

def infix_to_postfix(expr: str) -> str:
    # 연산자들을 잠시 보관할 스택
    op_stack = []
    # 결과(후위표기식)를 저장할 리스트
    output = []

    # 연산자 우선순위 딕셔너리 (곱하기가 더 우선순위 높음)
    prec = {'+': 1, '*': 2}

    # 수식 포문으로 돌면서
    for ch in expr:
        if ch.isdigit():
            # 숫자면 그냥 결과에 바로 넣는다
            output.append(ch)
        else:
            # 연산자라면 스택을 확인한다
            # 스택에 있는 연산자가 나보다 우선순위가 높거나 같으면 꺼내서 출력
            while op_stack and prec[op_stack[-1]] >= prec[ch]:
                output.append(op_stack.pop())
            # 그리고 지금 연산자는 스택에 넣기
            op_stack.append(ch)

    # 다 읽고 나면 스택에 남은 연산자를 전부 꺼내 결과에 붙인다
    while op_stack:
        output.append(op_stack.pop())

    return ''.join(output)


def eval_postfix(postfix: str) -> int:
    # 숫자들을 쌓아둘 스택
    stack = []

    # 후위표기식을 왼쪽부터 하나씩 본다
    for ch in postfix:
        if ch.isdigit():
            # 숫자는 스택에 넣는다 (push)
            stack.append(int(ch))
        else:
            # 연산자를 만나면, 숫자 2개를 스택에서 꺼낸다(pop)
            # 주의: 꺼낸 순서! 마지막이 오른쪽, 그 전이 왼쪽
            b = stack.pop()
            a = stack.pop()

            # 연산을 하고 결과를 다시 스택에 넣는다
            if ch == '+':
                stack.append(a + b)
            elif ch == '*':
                stack.append(a * b)

    # 마지막에 스택에 남은 하나가 정답
    return stack.pop()



for tc in range(1, 11):   # 문제 조건: 테스트케이스 10개
    _ = int(input())      # 수식 길이 받은거
    expr = input().strip() # 계산해야할 식 ㄷㄷ

    # 1. 후위표기식으로 바꾸기
    postfix = infix_to_postfix(expr)

    # 2. 후위표기식 계산하기
    answer = eval_postfix(postfix)

    print(f"#{tc} {answer}")
