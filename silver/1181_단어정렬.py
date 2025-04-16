# 직접구현 => 시간초과

# words = []
# for _ in range(int(input())):
#     w = input().strip() # 앞뒤 공백 제거
#     if w not in words:
#         words.append(w)

# n = len(words)
# for i in range(n):
#     for j in range(n - i - 1):
#         # 첫 번째 기준 : 길이
#         if len(words[j]) > len(words[j+1]):
#             words[j], words[j+1] = words[j+1], words[j]
#         # 두 번째 기준 : 사전 순
#         elif len(words[j]) == len(words[j+1]) and words[j] > words[j+1]:
#             words[j], words[j+1] = words[j+1], words[j]

# for w in words:
#     print(w)

# # set으로 중복 제거(O(1) 시간) => 그래도 시간초과과
# seen = set()
# words = []
# for _ in range(int(input())):
#     w = input().strip() # 앞뒤 공백 제거
#     if w not in words:
#         seen.add(w)
#         words.append(w)

# n = len(words)
# for i in range(n):
#     for j in range(n - i - 1):
#         # 첫 번째 기준: 길이
#         if len(words[j]) > len(words[j + 1]):
#             words[j], words[j + 1] = words[j + 1], words[j]
#         # 두 번째 기준: 사전 순
#         elif len(words[j]) == len(words[j + 1]) and words[j] > words[j + 1]:
#             words[j], words[j + 1] = words[j + 1], words[j]

# for w in words:
#     print(w)

# 정렬을 효율적인 sorted()로 변경
seen = set()
words = []
for _ in range(int(input())):
    w = input().strip()
    if w not in seen:
        seen.add(w)
        words.append(w)

# 첫 번째 기준 len(x) = 길이, x = 사전
words = sorted(words, key=lambda x: (len(x), x))

for w in words:
    print(w)

