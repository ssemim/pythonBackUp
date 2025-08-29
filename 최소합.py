import heapq

# 힙으로 사용할 배열
heap = []

lst = [6, 5, 4, 1, 3, 2, 9, 8, 7, 10]

for i in range(10):
    heapq.heappush(heap, lst[i])

for i in range(10):
    print(heapq.heappop(heap), end=" ")
print()
