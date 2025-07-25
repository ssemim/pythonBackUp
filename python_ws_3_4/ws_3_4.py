number_of_people = 0


def increase_user():
    global number_of_people
    number_of_people += 1


name = ['김시습', '허균', '남영로', '임제', '박지원']
age = [20, 16, 52, 36, 60]
address = ['서울', '강릉', '조선', '나주', '한성부']


def create_user(i):
    increase_user()

    return {
        'name': name[i],
        'age': age[i],
        'address': address[i]
    }


user_info = list(map(create_user, range(len(name))))




print( "총 사용자 수 : ", number_of_people)

for user in user_info:
    print(f"{user['name']}님 환영합니다!")

print(user_info)
