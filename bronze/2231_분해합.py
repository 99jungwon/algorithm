N = int(input())

# 생성자 구하기 생성자 = N + 각 자리수

for i in range(1, N):
    if i + sum(map(int, str(i))) == N:
        print(i)
        break
else:
    print(0)
