import sys
input = sys.stdin.readline

N = int(input())

queue = list(range(1, N+1))
start = 0 # 앞에서 pop 대신 인덱스로 처리

while start < len(queue) - 1:
    start += 1 # 맨 앞카드 버리기(start 인덱스 증가)
    queue.append(queue[start]) # 그 다음 카드를 맨 뒤로
    start += 1 # 앞에 꺼는 사용했으니 다시 증가

print(queue[start])