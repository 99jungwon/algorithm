N, K = map(int, input().split())

# 약수 구하기
# temp = []
# for i in range(1, N+1):
#     if N % i == 0:
#         temp.append(i)

# if K > (len(temp)):
#     print("0")
# else:
#     print(temp[K-1]

count = 0
for i in range(1, N+1):
    if N % i == 0:
        count += 1
        if count == K:
            print(i)
            break
else:
    print(0)