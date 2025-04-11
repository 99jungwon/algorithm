s = input()
result = []

for a in "abcdefghijklmnopqrstuvwxyz":
    idx = -1
    for i in range(len(s)):
        if s[i] == a:
            idx = i
            break
    result.append(str(idx)) # 

print(" ".join(result))