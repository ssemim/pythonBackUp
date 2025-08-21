N = 10  # 원형큐

CQ = [0] * 10

front = rear = 0


# 원형큐는 front를 위한 자리 1개를 비워둔다.

def is_full():
    return (rear + 1) % N == front


for i in range(1, 11):
    if not is_full():
        rear = (rear + 1) % N
    CQ[rear] = i

print(CQ, front, rear)
# 원형 큐에서 프론트를 위해 비워 둔 자리는 고정된 자리가 아니다
# 가득 찼을때와 아닐때를 구분하기 위해서 프론트자리하나 비워놓은거라니깐

for i in range(9):
    front = (front + 1) % N
    print(CQ[front], end=",")
print()

# 대가리 꼬리 번호 같으면 비어있는거라니깐
# ㅆ ㅂ 말투 왜 나루토말투 되어있는거냐

# front를 위해 비워둔 자리는 삭제할 때 마다 바뀐다
print(CQ, front, rear)
