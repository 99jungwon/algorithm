a = int(input())
b = int(input())
c = int(input())

result = str(a * b * c)
count = [0] * 10

for digit in result:
    for i in range(10):
        if digit == str(i):
            count[i] += 1

for c in count:
    print(c)