lst = [1,2,3]
N = 3

# 자리의 주인을 지목하는 방식
# 완성된 순열의 길이도 3
# 0번 인덱스에 누가올래? : make_perm(0)
# 1번 인덱스에 누가올래? : make_perm(1)
# ...

# N-1번 인덱스에 누가올래? : make_perm(N-1)
# N번 인덱스에 누가올래?? : make_perm(N) => XXXX 재귀 중단
# idx : 완성된 순열의 idx번 자리에 사용할 원소 선택
# selected : 순열을 만들때 이전에 사용한 원소는 사용불가, 체크용
# selected[x] == 1 : x번 원소는 이전에 순열만들때 사용함
# selected[y] == 0 : y번 원소는 이전에 사용한적없음 => idx 자리에 y번 원소가 올 수 있다.
# result : idx단계까지 완성된 순열(리스트, 문자열)
def make_perm(idx, selected, result):

    # 1. 종료 조건
    if idx == N:
        # 지금까지 만든 순열
        print(result)
        return

    # 2. 재귀 호출
    # idx 번 자리에 누가 올거냐? 선택
    # N개중에 하나 선택할껀데 => 이전에 선택한적 있는 원소는 선택하면 안된다.
    for i in range(N):
        # i번 원소를 이전에 순열만들때 쓴적 없다 => 순열의 idx번 위치에 올수 있다.
        if not selected[i]:
            # 순열의 idx번 자리에 i번 원소를 놓고 idx+1번 자리에 누가 올지 고민
            selected[i] = 1
            # 순열 만들기, lst의 i번 원소를 사용
            result.append(lst[i])
            make_perm(idx+1, selected, result)

            # i번 원소를 idx자리에 놓은 경우의수는 모두 고려 완료
            # i+1번 원소를 놓기 시작, i번원소는 사용하지 않았다 로 고쳐야 한다.
            selected[i] = 0
            result.pop()

# 0번 자리에 누가올지, 아직 아무도 고른적없고, 순열은 미완성(비어있는상태) 로 시작
make_perm(0,[0] * N, [])








