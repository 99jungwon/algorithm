T = int(input())

for _ in range(T):
    # 층수, 방수, 손님번호
    H, W, N = map(int, input().split())

    # 손님 번호가 층의 배수이면
    if N % H == 0:
        floor = H
        room = N // H
    else:
        floor = N % H
        room = N // H+1
    print(floor * 100 + room)
