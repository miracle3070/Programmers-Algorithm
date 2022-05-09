# 성공 (재도전)
# 풀이시간: 25분
# 메모: 변수 이름(phone2)을 잘못적는 바람에 오래걸렸음.
# 교훈: 숫자 문자열을 오름차순 정렬하면 길이에 상관없이 앞자리가 작은 문자열이 앞쪽으로 정렬된다.

import heapq
def solution(phone_book):
    heapq.heapify(phone_book)
    length = len(phone_book)
    phone1 = heapq.heappop(phone_book)
    for _ in range(length - 1):
        phone2 = heapq.heappop(phone_book)
        if phone2.startswith(phone1):
            return False
        phone1 = phone2  # phone2를 phone1로 적는 바람에 삽질해서 오래 걸림.

    return True
