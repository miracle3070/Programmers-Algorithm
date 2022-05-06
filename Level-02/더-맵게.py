# 풀이시간: 15분
import heapq


def solution(scoville, K):
    h = []
    for s in scoville:
        heapq.heappush(h, s)
    answer = 0
    while True:
        for s in h:  # 모든 스코빌 지수가 K 이상인지 확인
            if s < K:
                break
        else:  # 모든 스코빌 지수가 K 이상이면 while문 탈출
            break

        if len(h) <= 1:  # 힙의 길이가 1이하면서 스코빌 지수가 K 미만이면 -1을 반환
            answer = -1
            break
        s1 = heapq.heappop(h)
        s2 = heapq.heappop(h)
        mix_s = min(s1, s2) + (max(s1, s2) * 2)  # 새로운 스코빌 지수 계산
        heapq.heappush(h, mix_s)
        answer += 1  # 섞은 횟수 +1 증가

    return answer
