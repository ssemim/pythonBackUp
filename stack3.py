T = int(input())

for tc in range(1, T + 1):
    # 괄호검사 대상 코드
    code = input()

    # 스택
    s = []

    # 괄호검사 결과
    # 1 => ok // 0 => err
    answer = 1

    # 문자열을 순회 하면서 한글자씩 확인
    for c in code:
        # code 에서 한글자 떼어와서 c라고하자
        # 1. c가 여는 괄호 ({ 중 하나인경우 => stack 에 push
        if c in "{(":
            s.append(c)

        # 2. c가 닫는 괄호 )} 중 하나인경우 => stack 에서 pop
        # pop 하기 전에 스택이 비어있으면 안된다.
        # 왜? 스택이 비어있다는 것은 여는 괄호보다 닫는 괄호가 많았다
        # 괄호가 잘못되어있다.
        if c in ")}":
            # 스택s가 비어있나요?
            if not s:
                # 괄호가 잘못되어있다.(오른쪽괄호, 닫는괄호가 더 많음)
                answer = 0
                break
            # 스택s가 비어있지 않으면
            # 여는 괄호가 남아있다. => 꺼내서 확인
            left = s.pop()
            # left 와 c 비교해서 같은 종류의 괄호인지
            if not ((left == "(" and c == ")") or (left == "{" and c == "}")):
                # 괄호가 잘 되어있는 경우가 두가지인데
                # 두가지중 하나가 아닌경우 => 괄호가 잘못 짝지어져있다는것
                answer = 0
                break

            # 왼쪽 괄호의 짝이 c가 맞나요?
            pair = {"(": ")", "{": "}"}
            if pair[left] != c:
                # 짝이 안맞으면 괄호가 잘못되어있음
                answer = 0
                break

    # 3. 문자열을 다 검사했는데 스택에 뭔가 남아있다
    # 왼쪽 괄호, 여는괄호의 수가 오른쪽괄호, 닫는괄호보다 많았다
    # 괄호가 잘못되어있다.
    if len(s) > 0:
        answer = 0

    print(f"#{tc} {answer}")
