N = int(input())
n = N
count = 0

while True:
    tens = n // 10
    ones = n % 10
    temp = tens + ones
    n = (ones * 10) + (temp % 10)  
    count += 1                     
    if n == N:                     
        break

print(count)
