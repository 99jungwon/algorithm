import sys

n = int(sys.stdin.readline()) # 명령어 개수
commands = [sys.stdin.readline().strip() for _ in range(n)] # 명령어 리스트

stack = []

for cmd in commands:
    if cmd.startswith("push"):
        # 공백 기준으로 나누기
        # 'push X' -> ['push', 'X']
        _, num = cmd.split() 
        stack.append(int(num))
    elif cmd == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif cmd == "size":
        print(len(stack))
    elif cmd == "empty":
        # 스택이 안비었으면 0
        # 스택이 비어있으면 1
        print(0 if stack else 1)
    elif cmd == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)
