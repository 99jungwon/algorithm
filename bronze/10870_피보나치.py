# 피보나치
# n = int(input())

# num_1 = 0
# num_2 = 1
# total = 0
# if n == 0:
#     print(0)
#     exit()
# elif n == 1:
#     print(1)
#     exit()

# for _ in range(n-1):
   
#     total = num_1 + num_2
#     num_1 = num_2
#     num_2 = total

# print(total)

n = int(input())

a, b = 0, 1
for _ in range(n):
    a, b = b, a + b

print(a)