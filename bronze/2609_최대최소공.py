def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a
    
def lcm(a, b):
    return a * b // gcd(a,b)

num_1, num_2 = map(int, input().split())

print(gcd(num_1, num_2))
print(lcm(num_1, num_2))

