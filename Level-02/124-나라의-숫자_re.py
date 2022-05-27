# 실패
# 풀이시간: 30분

def changeNum(n):
    if n == 0:
        return "0"
    result = ""
    while n > 0:
        r = n % 3
        n //= 3
        result += str(r)
    return result[::-1]


def solution(n):
    answer = changeNum(n-1)
    if len(answer) == 1:
        if answer == "0":
            answer = "1"
        elif answer == "1":
            answer = "2"
        elif answer == "2":
            answer = "4"
    else:
        temp = answer[0]
        answer = answer[1:].replace("2", "4")
        answer = answer.replace("2", "1")
        answer = answer.replace("0", "1")
        answer = temp + answer
    return answer