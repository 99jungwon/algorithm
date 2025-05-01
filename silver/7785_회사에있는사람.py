import sys

n = int(sys.stdin.readline())
employees = set()

for _ in range(n):
    name, status = sys.stdin.readline().split()
    if status == 'enter':
        employees.add(name)
    else:
        employees.discard(name)

for name in sorted(employees, reverse=True):
    print
