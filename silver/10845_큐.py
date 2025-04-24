# 큐
# FIFO(First In First Out) 자료구조
# 선입선출 구조

import sys
input = sys.stdin.readline

N = int(input())
queue = []
start = 0

for _ in range(N):
    cmd = input().split()

    if cmd[0] == "push":
        queue.append(int(cmd[1]))
    elif cmd[0] == "pop":
        if start < len(queue):
            print(queue[start])
            start += 1
        else:
            print(-1)
    elif cmd[0] == "size":
        print(len(queue) - start)
    elif cmd[0] == "empty":
        print(0 if start < len(queue) else 1)
    elif cmd[0] == "front":
        print(queue[start] if start < len(queue) else -1)
    elif cmd[0] == "back":
        print(queue[-1] if start < len(queue) else -1)