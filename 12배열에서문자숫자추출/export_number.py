"""
문제

문자열 my_string이 매개변수로 주어집니다. my_string안의 모든 자연수들의 합을 return하도록 solution 함수를 완성해주세요.
"""
# 정규표현식 모듈
import re

# 문자열 중 문자와 숫자를 구분하여 리스트로 변환
print(re.findall("\d+", "hello123")) # ['123']
# 모듈 사용하지 않고 구현
my_string = "hello123"
my_list = []
for i in my_string:
    if i.isdigit():
        my_list.append(i)


# 문자열 중 문자만 추출
print(re.findall("\D+", "hello123")) # ['hello']
# 모듈 사용하지 않고 구현
my_string = "hello123"
my_list = []
for i in my_string:
    if i.isalpha():
        my_list.append(i)