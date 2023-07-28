"""
문제

문자열로 수식이 주어질 때(+, - 만 존재), 계산한 결과값을 출력하시오.
"""


def solution(my_string):
    return sum(int(i) for i in my_string.replace(' - ', ' + -').split(' + '))