# https://programmers.co.kr/learn/courses/30/lessons/42746?language=python3
def solution(numbers):

    # 맨 처음숫자가 가장 큰 순서대로 나열하면됩니다.
    numbers = list(map(str,numbers))
    # 리시트를 정렬하여 비교함.
    answer = sorted(numbers,key=lambda x : x*3 , reverse=True)
    # 리스트 항목들을 join을 통해 나열
    z = "".join(answer)
    # 값이 0일경우 string으로 리턴
    return z if int(z) != 0 else "0"
