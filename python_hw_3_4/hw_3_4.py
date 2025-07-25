import math 

# 1. 절댓값을 반환하는 함수 abs를 사용하여 아래 변수에 담긴 값의 절댓값을 출력하시오.
negative = -3

print(abs(negative))


# 2. 아래 변수에 담긴 값의 boolean 값을 출력하시오.
empty_list = []

print(bool(empty_list))

# 3. 주어진 리스트가 가진 모든 값을 더한 결과를 출력하시오.
# sum 사용하지 않고?  랜덤 숫자라고 생각했을 때, 주머니 안에 있는 공에 적혀있는 값들의 합은?
my_list = [1, 2, 3, 4, 5]

# "하나 꺼내서 더하고, 두번째 꺼내서 더하고, 마지막까지 반복... 
# 리스트를 순회하며 누적합 구하기

# t =0 
# lst = [3,6,7,1]
total = 0

for i in range(len(my_list)) :  
    total = total + my_list[i] 
    i =+ 1
    

print(total)

# for ball in lst:
#     t += ball

# print(t, sum(lst))



# 4. 주어진 정렬을 오름차순으로 정렬한 결과를 출력하시오.
unsorted_list = ['하', '교', '캅', '의', '지', '가']
unsorted_list.sort()
print(unsorted_list)