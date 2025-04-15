N, M = map(int, input().split)
board = [input() for _ in range(N)]

# 왼쪽 위가 W면 => (짝수칸 W, 홀수칸 B)
# 왼쪽 위가 B면 => (짝수칸 B, 홀수칸 W)
# 짝수 칸은 같은색, 홀수 칸은 다른색

def count_repaint(x, y): # x, y가 좌상단 시작위치
    repaint_w = 0 # 'W'로 시작한 경우 바꿔야 하는 칸 수
    repaint_b = 0 # 'B'로 시작한 경우 바꿔야 하는 칸 수

    for i in range(8):
        for j in range(8):
            current = board[x+i][y+i]

            if (i + j) % 2 == 0:
                # 짝수 = 같은 색
                if current != 'W':
                    repaint_w += 1
                if current != 'B':
                    repaint_b += 1
            else:
                if current != 'B':
                    repaint_w += 1
                if current != 'W':
                    repaint_b += 1
    return min(repaint_w, repaint_b)

# 가능한 모든 8x8 구간에서 최소 잘할 칸 수 찾기
min_repaint = float('inf')

for i in range(N - 7): # 세로 시작 인덱스
    for j in range(M - 7): # 가로 시작 인덱스
        min_repaint = min(min_repaint, count_repaint(i, j))

print(min_repaint)