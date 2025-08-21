# 파이썬의 리스트 메서드를 사용해서 큐 만들기

# 큐로 사용할 리스트

q = []

for i in range(1, 4):
    q.append(i)

print(q)

# 원소 삭제하기

for i in range(3):
    print(q.pop(0), end=",")
print()

# 이거 쓰지 말라고 하는 이유는, 배열이 길면 길수록 일일히 다 옮겨 와야하기때문에 (N-1)번 옮겨야함
# 몇 개 안될땐 쓸 수 있는데,케이스 많으면 시간초과 뜰 듯


print(q)