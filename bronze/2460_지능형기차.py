max_people = 0
temp = 0

for _ in range(10):
    out_people, in_people = map(int, input().split())
    temp = temp - out_people + in_people
    if max_people < temp:
        max_people = temp
print(max_people)