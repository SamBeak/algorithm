"""
문제

이진수를 의미하는 두 개의 문자열 bin1과 bin2가 매개변수로 주어질 때, 두 이진수의 합을 return하도록 solution 함수를 완성해주세요.
"""

def solution(bin1, bin2):
    return bin(int(bin1, 2) + int(bin2, 2))[2:] # int(bin1,2)에서 2는 2진수를 의미한다. 8진수는 8, 16진수는 16.
#[2:]은 0b를 제거하기 위함이다. 0b101 이렇게 나오기 때문에.