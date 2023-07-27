"""
문제
문자열 my_string 이 주어질 때, 중복을 제거하고 출력
"""

def solution(my_string):
    return "".join([value for idx, value in enumerate(my_string) if value not in my_string[:idx]])

"""
# 문자열 중복제거 (list comprehension을 이용)
print([value for index, value in enumerate(my_string) if value not in my_string[:index]])
"""