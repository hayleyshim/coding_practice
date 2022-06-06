"""
문제 설명 : 정수를 담고 있는 배열 arr의 평균값을 return하는 함수, solution을 완성해보세요.
제한사항

- arr은 길이 1 이상, 100 이하인 배열입니다.
- arr의 원소는 -10,000 이상 10,000 이하인 정수입니다.
"""

def solution(arr):
    answer = 0

    answer = sum(arr)
    answer = answer/len(arr)

    return answer


arr = [1,2,3,4]

print(solution(arr))

"""
simple is the best 
"""

def average(list):
    return (sum(list) / len(list))

# 아래는 테스트로 출력해 보기 위한 코드입니다.
list = [5,3,4]
print("평균값 : {}".format(average(list)));

