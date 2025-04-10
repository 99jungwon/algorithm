N = int(input()) # 숫자 개수
# 입력 받은 개수만큼 리스트 저장
nums = [int(input()) for _ in range(N)]

for i in range(N):
    for j in range(N - i - 1):
        if nums[i] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]

for num in nums:
    print(num)
