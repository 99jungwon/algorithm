T = int(input())

for _ in range(T):
    n = int(input())

    temp = []
    while n > 0:
        temp.append(n % 2)
        n = n // 2
    for i in range(len(temp)):
        if temp[i] == 1:
            print(i, end=' ')
    print()  # 테스트케이스 구분을 위한 줄바꿈
