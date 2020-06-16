# https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
def solution(phone_book):
    answer = True
    phone_book.sort()

    for i in range(len(phone_book)-1):
        if phone_book[i] in phone_book[i+1]:
            answer = False
            break
        else:
            answer = True
    return answer
