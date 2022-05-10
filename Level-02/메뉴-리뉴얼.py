# 실패 (시간초과)
# 풀이시간: 28분
# 메모: 조합(combinations)를 다루는데에 익수하지 않았다. / 효율적인 코드가 아니어서 시간초과 발생.

from itertools import combinations

def solution(orders, course):
    answer = []
    menus = set()
    for order in orders:
        menus = menus | set(order)

    # 단품 개수에 따라 결과값 도출
    for c in course:
        temp = []
        cases = combinations(menus, c)
        for case in cases:
            cnt = 0
            for order in orders:
                for ch in case:
                    if ch not in order:
                        break
                else:
                    cnt += 1
            case = list(case)
            case.sort()
            temp.append(("".join(case), cnt))
        temp.sort(reverse=True, key=lambda x:x[1])
        if temp[0][1] < 2:
            continue
        check = temp[0][1]
        for t in temp:
            if t[1] < check:
                break
            answer.append(t[0])

    answer.sort()
    return answer