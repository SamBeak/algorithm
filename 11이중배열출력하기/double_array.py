"""
문제

정수 배열 num_list와 정수 n이 매개변수로 주어집니다. num_list를 다음 설명과 같이 2차원 배열로 바꿔 return하도록 solution 함수를 완성해주세요.
"""

def double_array_fundamental(arr,n):
    double_array = [arr[i:i+n] for i in range(0, len(arr), n)]
    return double_array