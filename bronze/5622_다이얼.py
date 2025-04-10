# 숫자 1은 2초
# 한 칸 옆에 있는 숫자는 1초씩 더 걸림
# 1
# 2 = abc, 3 = def, 4 = ghi
# 5 = jkl, 6 = mno, 7 = pqrs
# 8 = tuv, 9 = wxyz

word = input()
time = 0

for ch in word:
    if ch in 'ABC':
        time += 3
    elif ch in 'DEF':
        time += 4
    elif ch in 'GHI':
        time += 5
    elif ch in 'JKL':
        time += 6
    elif ch in 'MNO':
        time += 7
    elif ch in 'PQRS':
        time += 8
    elif ch in 'TUV':
        time += 9
    elif ch in 'WXYZ':
        time += 10

print(time)
