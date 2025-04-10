N = int(input())
num_list = list(map(int, input().split()))

min_val = num_list[0]
max_val = num_list[0]
for num in num_list:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

print(min_val, max_val)
