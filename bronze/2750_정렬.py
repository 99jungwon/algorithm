N = int(input()) # 숫자 개수
nums = [int(input()) for _ in range(N)] # 입력 받은 개수만큼 리스트 저장

for i in range(N):
    for j in range(N - i - 1):
        if nums[i] > num[j + 1]:

