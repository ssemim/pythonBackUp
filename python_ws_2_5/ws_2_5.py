from copy import deepcopy


catalog = [
    ['시간의 틈', '반짝임의 어둠', '망각의 경계'],
    ['연기의 수수께끼', '장면의 고백', '드라마의 그림자'],
    ['황금의 칼날', '비열한 간신', '무명의 영웅'],
    ['성공의 열쇠', '내면의 변화', '목표의 달성'],
]

backup_catalog = catalog.copy() # 얕은 복사로 껍질은 복사되지만, 내용은 같은 것을 참조
backup_catalog = deepcopy(catalog) # 깊은 복사로 내용까지 복사


# 깊다는 리스트 안에 리스트 안에 리스트 안에 ...
#얕다는 카탈로그의 카피 기능을 써서 한방에

''' 
도서 제목 '성공의 열쇠', '내면의 변화', '목표의 달성' 을 각각
'성공을 향한 한 걸음', '내 삶의 변화', '목표 달성의 비밀' 가 되도록 변경하시오.
'''

print('catalog와 backup_catalog를 비교한 결과')
# 식별 연산자로 catalog와 backup_catalog를 비교한 결과를 출력하시오.
print()
print(catalog is backup_catalog)
print('backup_catalog : ')
print(backup_catalog)
print()

print('catalog : ')
print(catalog)
