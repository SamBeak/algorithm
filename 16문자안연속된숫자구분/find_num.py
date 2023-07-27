"""
문제

문자와 숫자로 된 문자열 중 숫자의 합 구하기, 연속된 숫자 인식
"""

def solution(my_string):
    s = ''.join(i if i.isdigit() else ' ' for i in my_string)
    return sum(int(i) for i in s.split())