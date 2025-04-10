N = int(input())

# 1층 올라 갈때마다 6, 12, 18 층마다 필요한 방의 개수가 증가

count = 1 # 층
range = 1 # 총 방의 개수
while N > range:
    range = range + (count * 6)
    count += 1
print(count)