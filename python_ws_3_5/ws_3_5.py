rentaled_books = 0
number_of_book = 100
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

for user in user_info:
    print(f"{user['name']}님 환영합니다!")


many_user = list(map(lambda user: {
    **user,
    'books': user['age'] // 10
}, user_info))

def rental_book(info):
    global rentaled_books, number_of_book
    rentaled_books += info['books']
    number_of_book -= info['books']
    print(f"남은 책 수: {number_of_book} \n{info['name']}님이 책 {info['books']}권을 대여하였습니다. ")



# rental_book을 many_user 각각에 적용
list(map(rental_book, many_user))

