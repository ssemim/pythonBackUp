# front와 rear를 사용해서 큐 만들기

# 큐의 크기

N = 3

# 공백 상태의 큐를 생성

q = [0] * N

front = rear = -1
# front : 마지막에 삭제한 원소의 위치
# rear : 마지막에 삽입한 원소의 위치

# 1, 2, 3 삽입하기

for i in range(1, 4):
    # 가장 마지막에 삽입한 원소의 한 칸 뒤에 삽입을 해야함
    rear += 1
    q[rear] = i

print(q)

# 원소 삭제 3번

for i in range(3):
    # 가장 마지막에 삭제한 원소의 위치 +1에 있는 원소를 새로 삭제해줘야하므로
    front += 1
    print(q[front], end=",")
print()

print(q,front,rear)
# 삭제를 해도 출력에는 1,2,3이 출력이 된다 왜지 => 리스트처럼 쓰지 말라고 했거던
# front와 rear값만 보고 판단을 해야한다는 뜻이야
# front와 rear값이 똑같으니까 큐가 비었다고 생각해야해

rear += 1
q[rear]

# 선형 큐 구조상 계속 땡겨오면 또 길이 횟수만큼 땡겨야해서 준니 느려진다

