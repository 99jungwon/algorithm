remainders = set() # 중복이 제거됨

for _ in range(10):
    num = int(input())
    remainders.add(num % 42)

print(len(remainders)) # 중복이 제거된 길이 출력
