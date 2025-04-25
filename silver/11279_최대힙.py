import sys

input = sys.stdin.readline

N = int(input())
heap = []
result = []

def push(x):
    heap.append(x)
    idx = len(heap) - 1
    while idx > 0:
        parent = (idx - 1) // 2
        if heap[parent] < heap[idx]:  # 여기 수정
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent
        else:
            break

def pop():
    if not heap:
        return 0
    max_value = heap[0]
    last_value = heap.pop()
    if heap:
        heap[0] = last_value
        idx = 0
        size = len(heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            largest = idx

            if left < size and heap[left] > heap[largest]:  # 여기 수정
                largest = left
            if right < size and heap[right] > heap[largest]:  # 여기 수정
                largest = right

            if largest == idx:
                break

            heap[idx], heap[largest] = heap[largest], heap[idx]
            idx = largest
    return max_value

for _ in range(N):
    x = int(input())
    if x == 0:
        result.append(str(pop()))
    else:
        push(x)

print('\n'.join(result))
