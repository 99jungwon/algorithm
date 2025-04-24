import sys
input = sys.stdin.readline

n = int(input())
sequence = [int(input()) for _ in range(n)]

stack = []
result = [] # +, - 결과 저장용
current = 1 # 1부터 시작해서 차례대로 push할 숫자
idx = 0 # 수열에서 비교할 위치

for target in sequence:
    while current <= target:
        stack.append(current)
        result.append('+')
        current += 1

    if stack[-1] == target:
        stack.pop()
        result.append('-')
    else:
        print('NO')
        sys.exit(0)

for r in result:
    print(r)