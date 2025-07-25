import random

lst = random.choices(range(10),k=5)

#리스트 길이 
l = len(lst)

MAX_V = lst[0]

print("리스트 : ", lst)

#리스트를 순회하면서 최대값 구하기

for i in range(l) :

    if MAX_V<lst[i] :
        MAX_V = lst[i]
    else : None

print(MAX_V)



