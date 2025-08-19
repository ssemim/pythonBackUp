# 스택 밖에 있을때 우선순위
icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
# 스택 안에 있을때 우선순위
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}


# 중위표기식을 후위표기식으로 바꾸기
# infix : 중위표기식
# N : 식의 길이(토큰의 개수)
def get_postfix(infix, N):
    # 결과로 출력할 후위표기식
    postfix = ""

    stack = []

    # 중위표기식에서 글자(토큰) 하나씩 떼어와서 후위표기식을 만들자
    for token in infix:
        # 토큰이 피연산자인경우
        if token not in "()+-*/":
            # 후위표기식에 그대로 피연산자를 쓴다.(출력한다)
            postfix += token
        # 토큰이 연산자인경우
        else:
            # 토큰이 ")" 라면
            if token == ")":
                # "( ... )" 안에 있는 모든 연산자가 먼저 계산이 되어야한다.
                # 스택안에 "(" 를 만날때까지 모든 연산자를 꺼내 쓴다.
                while stack:
                    # 연산자를 하나 꺼내보기
                    operator = stack.pop()
                    # 꺼낸게 "(" 라면 연산자 꺼내기 중단
                    if operator == "(":
                        break
                    # 여는괄호가 아니면 계속 식에 출력
                    postfix += operator
            # 토큰이 닫는 괄호가 아닌 다른 연산자였다면
            else:
                # 스택 꼭대기에 있는 연산자의 우선순위와 => isp[stack[-1]]
                # 현재 토큰의 우선순위를 비교 => icp[token]
                # 누가더 우선순위가 높은지 확인
                # 우선순위가 높은 연산자는 먼저 계산이 되야하니까 출력하기

                # 스택안에 현재 token 보다 우선순위가 같거나 높은 연산자는 다 꺼내쓴다
                while stack and icp[token] <= isp[stack[-1]]:
                    # 꺼내서 결과에 이어붙이기
                    postfix += stack.pop()

                # token의 우선순위가 스택의 꼭대기에 있는 연산자의 우선순위보다 높았다면
                # 또는 스택이 비어있다면
                stack.append(token)

    # 모든 토큰을 확인 한 후에 스택에 남아있는 연산자는 그대로 차례대로 출력
    while stack:
        postfix += stack.pop()

    return postfix


infix = "(6+5*(2-8)/2)"
postfix = get_postfix(infix, len(infix))
print(postfix)

# 후위표기식을 계산하는 함수
def get_result(postfix):
    # 계산방법
    # 토큰을 하나씩 쭉 읽는다.
    # 연산자를 만나면 제일 최근에 만난 피연산자 두개 가지고 연산
    # 스택에 피연산자를 저장

    stack = []

    for token in postfix:
        # 토큰 하나떼어와서

        # 피연산자라면
        if token not in "*/+-":
            # 스택에 넣기
            stack.append(int(token))  # 타입 조심
        # 연산자라면
        else:
            # 스택에서 두개 꺼내서 연산하고 그 결과값을 다시 스택에 넣기
            # 꺼내는 순서에 따라 연산자의 왼쪽인지 오른쪽인지
            # 먼저 꺼낸게 오른쪽
            right = stack.pop()
            left = stack.pop()

            # 연산자의 종류에 따라 계산
            result = 0

            if token == "+":
                result = left + right
            elif token == "-":
                result = left - right
            elif token == "*":
                result = left * right
            elif token == "/":
                result = left / right  # 연산 결과 정수? 실수?

            # 이 계산 결과도 나중에 다른 연산자의 피연산자로 사용 될 것
            stack.append(result)

    # 계산이 잘 진행되었다면 모든 토큰을 읽고 난 후에
    # 스택안의 상태가 ??
    return stack.pop()

result = get_result(postfix)
print(result)

