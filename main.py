def function1(a, b, c):
    print("1번 함수 시작", a, b, c)

    function2(a, b, c)

    print("1번 함수 종료", a, b, c)


def function2(a, b, c):
    print("2번 함수 시작", a, b, c)

    function3(a, b, c)

    print("2번 함수 종료", a, b, c)


def function3(a, b, c):
    print("3번 함수 시작", a, b, c)

    print("3번 함수 종료", a, b, c)


function1(1, 2, 3)
