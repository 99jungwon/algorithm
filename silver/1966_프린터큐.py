T = int(input())

for _ in range(T):
    # N:문서 개수, M:궁금한 문서의 인덱스스
    N, M = map(int, input().split())
    importance = list(map(int, input().split()))

    queue = [(i, p) for i, p in enumerate(importance)]
    order = 0 # 몇 번째로 출력되는지지

    while queue:
        cur = queue.pop(0)
        if any(cur[1] < item[1] for item in queue):
            queue.append(cur)
        else:
            order += 1
            if cur[0] == M:
                print(order)
                break