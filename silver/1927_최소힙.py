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
        if heap[parent] > heap[idx]:
            heap[parent], heap[idx] = heap[idx], heap[parent]
            idx = parent
        else:
            break

def pop():
    if not heap:
        return 0
    min_value = heap[0]
    last_value = heap.pop()
    if heap:
        heap[0] = last_value
        idx = 0
        size = len(heap)
        while True:
            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx

            if left < size and heap[left] < heap[smallest]:
                smallest = left
            if right < size and heap[right] < heap[smallest]:
                smallest = right

            if smallest == idx:
                break

            heap[idx], heap[smallest] = heap[smallest], heap[idx]
            idx = smallest
    return min_value

for _ in range(N):
    x = int(input())
    if x == 0:
        result.append(str(pop()))
    else:
        push(x)

print('\n'.join(result))
