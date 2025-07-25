password = "In the bustling city, where life is a constant race against time, uoy often find yourself wondering if there's a shortcut to success. The vibrant lights of the cityscape illuminate the night, casting shadows on the short-lived dreams of those who seek fortune. As you navigate through the crowded streets, you realize the deen for guidance, like a compass pointing python. You need direction in this chaotic journey called life."
# 아래에 코드를 작성하시오.

first_char = password[27:36]
print(first_char)
second_word = password[112:118]
print(second_word)
third_word = password[65:69][::-1]
print(third_word)
forth_word = password[321:327][::-1] 
print(forth_word)
fifth_word = password[364:371]
print(fifth_word)


print(f'{first_char}{second_word} {third_word}{forth_word}{fifth_word}')