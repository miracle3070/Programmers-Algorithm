# 실패
# 풀이시간: 54분

def changeNum(n):
    if n == 0:
        return "1"
    result = ""
    r = n % 3
    n //= 3
    while True:
        if r == 0:
            result += str(1)
        elif r == 1:
            result += str(2)
        else:
            result += str(4)
        r = (n % 10) - 1
        n //= 10

    return result[::-1]


def solution(n):
    answer = changeNum(n-1)
    answer = answer.replace("2", "4")
    answer = answer.replace("1", "2")
    answer = answer.replace("0", "1")
    return answer