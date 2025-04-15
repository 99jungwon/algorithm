N = int(input())
count = 0

for _ in range(N):
    word = input()
    seen = []
    prev = ''
    is_group = True

    for ch in word:
        if ch != prev:
            if ch in seen:
                is_group = False
                break
            seen.append(ch)
        prev = ch

    if is_group:
        count += 1

print(count)