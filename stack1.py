# 파이썬에서 리스트의 메서드를 사용하는 방법

# 빈 리스트를 만들고 이 리스트를 스택처럼 쓰겠다.

s = []

# 스택에 원소를 삽입 : push

for i in range(10):
    s.append(i)  # 리스트의 append()메서드를 통해 마지막에 추가

print(s)

print(s-1)

# 스택에서 원소를 삭제 : pop

for i in range(10):
    print(s.pop(), end=",")
print()

# s안에 뭔가가 남아있다면 반복이 계속된다.
# s 안에 아무것도 없다면 반복이 중단된다.
while s:
    print(s.pop(), end=" ")
print()

print(s)
