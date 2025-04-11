# 0층 : 1호 = 1명 2호 = 2명 3호 = 3명....
# 1층 : 1호 = 1명 2호 1 + 2 = 3명 3호 = 1 + 2 + 3 = 6명
# 2층 : 1호=1명 2호 1+3=4명 3호 1+3+6=10명
# .....

T = int(input()) # 테스트 케이스 개수

for _ in range(T):
    k = int(input()) # 층
    n = int(input()) # 호

    # 0층 리스트
    floor = [i for i in range(1, n+1)]

    # 1층부터 k층까지 계산
    for _ in range(k):
        new_floor = [] # 현재 층
        for i in range(n):
            # 1호부터 i호까지 사람 수 더하기
            new_floor.append(sum(floor[:i+1])) 
        floor = new_floor # 다음 층을 위한 갱신

    print(floor[n-1])
