# 이중순회 쌍 찾기 Dual Traversal Target Pair
# dual traversal은 알고리즘의 핵심 개념이다.

"""
문제
함수에 숫자 배열과 '특정수(target)'을 인자(Argument)로 넘기면,
더해서 '특정수(target)'이 나오는 index를 배열에 담아 return한다.
"""

nums = [4, 9, 11, 14] # 숫자 배열


def two_sum(arr, target):                               # parameter로 arr과 target 설정
    for i in range(len(arr)-1):                         # placeholder : i지만 range와 len의 조합으로 숫자 출력, 숫자 0 ~ 배열 길이-1까지 출력
        for j in range(len(arr)-(i+1)):                 # placeholder : j = i+1 //
            j+=(i+1)                                    # j = j + (i+1)   // 0  + (0 + 1) // 1 + (0 + 1)  // 2 + (0 + 1) ....
            if target == arr[i] + arr[j]:
                return [i, j]

print(two_sum(nums, 25))                                # arguments = nums, 25