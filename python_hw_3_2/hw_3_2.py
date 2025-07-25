# 아래 함수를 수정하시오.
def add_numbers():
    global number_a, number_b, answer

    number_a = input('첫 번쨰 숫자를 입력하세요 : ')
    number_b = input('두 번째 숫자를 입력하세요 : ')
    answer = int(number_a)+int(number_b)
    return 


# 수정한 add_numbers() 함수를 호출하시오.
add_numbers()
print(answer)