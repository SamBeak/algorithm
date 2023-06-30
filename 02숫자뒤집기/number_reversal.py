#  숫자 뒤집기 Number Reverse

"""
문제
Reverse 함수에 정수인 숫자를 인자로 받는다. 숫자를 뒤집어 return한다.
"""

number = input('input number: ')    # 숫자 입력, 문자열 전달

def reverse(num):
    number_int = int(num)
    if number_int < 0:                  # 음수에 대한 경우의 수
        number_int = -number_int        # 양수 치환
    number_str = str(number_int)        # 문자열 변환
    reverse_str = number_str[::-1]      # 슬라이싱, 역순
    reverse_number = int(reverse_str)   # 숫자 변환
    return reverse_number               # 결과 반환

print(reverse(number))