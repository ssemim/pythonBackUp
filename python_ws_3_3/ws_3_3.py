rentaled_books = 0
number_of_book = 100


def rental_book():
    global rentaled_books
    global name 
    name = input('대여자의 이름을 작성해 주세요 : ')  
    rentaled_books = input('몇 권 빌려갑니까? : ')

    rentaled_books = int(rentaled_books)



def decrease_book():
    global number_of_book
    
    print(f'남은 책의 수 : {number_of_book-rentaled_books}')
    print(f'{name}님이 {rentaled_books}권의 책을 대여하였습니다.' )


rental_book()
decrease_book()
    