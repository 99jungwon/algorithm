import sys

n = int(sys.stdin.readline()) # 명령어 개수
commands = [sys.stdin.readline().strip() for _ in range(n)] # 명령어 리스트

stack = []

for cmd in commands:
    if cmd.startwith("push"):
        _, num = cmd.split() # 공백 기준으로 나눠서 숫자만 추출