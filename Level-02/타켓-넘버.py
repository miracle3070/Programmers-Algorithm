# 풀이시간: 11분

def DFS(i, total):
    global cnt
    global target_num
    global num_list
    global answer
    if i == cnt:
        if total == target_num:
            answer += 1
        return
    else:
        DFS(i + 1, total + num_list[i])
        DFS(i + 1, total - num_list[i])


def solution(numbers, target):
    global cnt
    global answer
    global target_num
    global num_list
    target_num = target
    num_list = numbers
    cnt = len(numbers)
    answer = 0
    DFS(0, 0)

    return answer