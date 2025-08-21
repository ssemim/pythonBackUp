lst = [1, 2, 3, 4, 5]

N = 5
# 부분집합의 합이 5이하인 부분집합만 구하세요 -> S
S = 5


# 부분집합을 만드는 재귀함수
# make_set(0) : 0번 원소를 부분집합에 넣을지 말지
# make_set(1) : 1번 원소를 부분집합에 넣을지 말지
# make_set(N-1) : N-1번 원소를 부분집합에 넣을지 말지
# make_set(N) : N번 원소는 없으니까 => 재귀호출 중단

# idx : 내가 지금 idx번 원소를 원소에 넣을지 말지 넣는 그거임
# selected 리스트 : 내가 지금까지 부분집합에 포함할 원소들의 상태를 나타내는 변수
# selected 리스트 : 내가 지금까지 부분집합에 포함할 원소들의 상태를 나타내는 변수
# selected[x] == 1 (True) : x번 원소를 부분집합에 넣기로 했다. 반대로 ==0 이면 False 안넣는다는 뜻

# s : idx번 원소까지 부분집합에 넣을지 말지 고민을 하고 있는데, 이 때 까지 완성한 부분집합의 합
def make_set(idx, selected, s):
    # 재귀함수의 필수 두가지

    # 0 가지치기
    # 지금까지 구한 부분집합의 합 s 가
    # 문제에서 원하는 합 S보다 크면 더 진행 x (답이 될 확률이 없음)

    if s > S:
        return

        # 1. 종료조건
    if idx == N:
        # selected 배열을 보고 내가 어떤 원소를 선택했었는지 확인
        subset = []
        for i in range(N):
            # 내가 i번 원소를 부분집합에 포함하기로 했었다면
            if selected[i]:
                subset.append(lst[i])
            print(subset)
        if sum(subset) <= 5:
            print(subset)  # 이게 DFS임
        return

    # 2. 재귀 호출
    # idx번 원소를 부분집합에 넣고 idx+1번 원소를 판단하기
    # 먼저 선택한 코드를 선택하지 않은 코드보다 먼저 호출한다
    selected[idx] = 1
    make_set(idx + 1, selected)

    # idx번 원소를 부분집합에 넣지 않고 idx+1번 원소를 판단하기
    selected[idx] = 0
    make_set(idx + 1, selected)


make_set(0, [0] * N)  # 함수 불러서 ㄱㄱ
