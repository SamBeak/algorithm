"""
문제
배열 뒤집기 / reverse사용하지 않고 구현하기
"""

def reverse(arr):
    # 코드 작성
    return arr[::-1]

def solution(arr):
    result = []
    for i in range(len(arr)):
        result.append(arr[len(arr)-1-i])
    return result

def solution2(arr):
    result = []
    for i in range(len(arr)):
        result.append(arr.pop())
    return result

def solution3(arr):
    result = []
    while arr:
        result.append(arr.pop())
    return result
