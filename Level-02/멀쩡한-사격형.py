# 성공
# 풀이시간: 50분
# 메모: 처음 풀었을때 시간초과 계속 발생했었음. (W == 1 또는 H == 1일 경우에 0을 리턴할 생각을 못했었음.)

import math


def solution(w, h):
    if w == 1 or h == 1:
        return 0

    # 최대공약수 구하기
    common = 1
    for i in range(min(w, h) + 1, 1, -1):
        if w % i == 0 and h % i == 0:
            common = i
            break

    # 약분
    min_w = w // common
    min_h = h // common

    a = min_h / min_w  # 기울기
    count = 0
    prev_y = 0
    for x in range(1, min_w + 1):
        y = a * x
        count += math.ceil(y) - math.floor(prev_y)
        prev_y = y

    answer = w * h - (w // min_w * count)
    return answer