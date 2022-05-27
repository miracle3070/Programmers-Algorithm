# 실패 (시간초과)
# 풀이시간: 16분


def solution(s):
    string = list(s)
    cur = 0
    while cur < len(string):
        print("".join(string), cur)
        if len(string) == 0:
            return 1
        for i in range(cur, len(string)-1):
            if string[i] == string[i+1]:
                string = string[:i] + string[i+2:]
                cur = i - 1
                if cur < 0:
                    cur = 0
                break
        else:
            return 0
    return 1