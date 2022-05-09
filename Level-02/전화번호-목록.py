# 실패
# 메모: 시간초과 나옴.

def solution(phone_book):
    phone_book.sort(key=lambda x:len(x))
    for x in range(len(phone_book)):
        for y in range(x+1, len(phone_book)):
            if phone_book[y].startswith(phone_book[x]) == True:
                return False
    return True