"""
문제

가장 가까운 수 찾기
"""

def solution(array, n):
    answer= []
    array.sort()
    for i in range(len(array)):
        answer.append(abs(n-array[i]))
    for i in range(len(answer)):
        if answer[i] == min(answer):
            return array[i]