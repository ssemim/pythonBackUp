number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


increase_user()
print(number_of_people)
