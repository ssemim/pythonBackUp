def factorial(n):
    print("팩토리얼", n)

    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))
