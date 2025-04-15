N = int(input())
points = [list(map(int, input().split()))
          for _ in range(N)]

for i in range(N):
    for j in range(0, N - i - 1):
        x1, y1 = points[j]
        x2, y2 = points[j + 1]

        # x기준 오름차순, 같으면 y 기준 오름차순
        if x1 > x2 or (x1 == x2 and y1 > y2):
            points[j], points[j + 1] = points[j + 1], points[j]

for x, y in points:
    print(x, y)

# N = int(input())
# points = [list(map(int, input().split())) for _ in range(N)]

# points.sort()  # 기본: x 오름차순, x 같으면 y 오름차순

# for x, y in points:
#     print(x, y)
