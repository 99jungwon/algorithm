heights = []

for _ in range(9):
    num = int(input())
    heights.append(num)

total = sum(heights)
temp = total - 100

for i in range(9):
    for j in range(i+1, 9):
        if heights[i] + heights[j] == temp:
            a = heights[i]
            b = heights[j]
            heights.remove(a)
            heights.remove(b)
            heights.sort()
            for h in heights:
                print(h)
            exit()
