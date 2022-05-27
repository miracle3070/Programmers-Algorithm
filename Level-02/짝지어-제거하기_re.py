# 성공
# 풀이시간: 5분
# 메모: 스택을 써야한다는 인지하지 못해서 못풀었었음.

def solution(s):
    stack = []
    for ch in s:
        if len(stack) == 0:
            stack.append(ch)
        elif stack[-1] == ch:
            stack.pop()
        else:
            stack.append(ch)
    if len(stack) == 0:
        return 1
    else:
        return 0