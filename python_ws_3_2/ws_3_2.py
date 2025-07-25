number_of_people = 0
user_info = {}



def increase_user():
    global number_of_people
    number_of_people += 1

def create_user():

    global user_info
  
    name = input('이름을 입력하세요 : ')
    age = input('나이를 입력하세요 : ')
    address = input('주소를 입력하세요 : ') 

    user_info = {

        'name' : name, 
        'age' : age,
        'address' : address 

    }
    return user_info


increase_user()
create_user()

print(user_info)
print(f'현재 가입 된 유저 수 : {number_of_people}')