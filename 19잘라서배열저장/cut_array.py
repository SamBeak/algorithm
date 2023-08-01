# 문자열 my_str과 숫자 n이 주어질 때, 문자열을 n개씩 끊어 배열로 반환
def solution(my_str, n):
    return [my_str[i:i+n] for i in range(0, len(my_str), n)]