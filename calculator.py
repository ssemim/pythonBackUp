T = int(input())  # 테스트 케이스 받고

for test_case in range(1, T + 1):
    stack = [0] * 200  # 스택용 배열
    top = -1  # 탑 설정

    icp = {'(': 3, '*': 2, '/': 2, '+': 1, '-': 1}  # 밖에 있을 때의 우선 순위 (클수록 높음)
    isp = {'(': 0, '*': 2, '/': 2, '+': 1, '-': 1}  # 스택 안에 있을 때의 우선 순위

    infix = str(input())  # 일단 중위식 받고
    postfix = ''  # 변환할 후위식은 공란으로 두고

    for token in infix:
        if token not in '(+-*/)':  # 피연산자면 후위식에 추가
            postfix += int(token)
        elif token == ')':  # 여는 괄호를 만날 때까지 pop
            while top > -1 and stack[top] != '(':
                top -= 1
                postfix += stack[top + 1]
            if top != -1:  # 전체 수식이 괄호로 둘러 쌓이지 않은경우 대비
                top -= 1  # '(' 버림...
        else:  # 연산자인 경우
            if top == -1 or isp[stack[top]] < icp[token]:  # 토큰의 우선순위가 더 높으면
                top += 1  # push
                stack[top] = token
            elif isp[stack[top]] >= icp[token]:  # 토큰과 같거나 더 높으면
                while top > -1 and isp[stack[top]] >= icp[token]:
                    postfix += stack[top]
                    top -= 1
                top += 1  # push
                stack[top] = token
