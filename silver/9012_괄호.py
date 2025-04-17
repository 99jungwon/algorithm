import sys

T = int(sys.stdin.readline())
lines = [sys.stdin.readline().strip() for _ in range(T)]

for word in lines:
    stack = []
    is_vaild = True 
    
    for ch in word:
        if ch =='(': # 여는 괄호면 스택에 추가
            stack.append('(')
        else: # if ch ==')':
            if stack: # 스택이 비어있지 않으면
                stack.pop() # 삭제제
            else: # 스택이 비어있으면 짝이 안맞으니까
                is_vaild = False
                break # 애초에 False

    if stack: # 다 돌았는데 뭐가 남아있으면
        is_vaild = False # False
    print("YES" if is_vaild else "NO")