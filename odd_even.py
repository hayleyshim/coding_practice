"""
문제 설명 : 정수 num이 짝수일 경우 "Even"을 반환하고 홀수인 경우 "Odd"를 반환하는 함수, solution을 완성해주세요.
제한 조건
- num은 int 범위의 정수입니다.
- 0은 짝수입니다.
"""

def solution(num):
    if num%2 == 1:
        return "Odd"
    else:
        return "Even"


solution(4)
solution(3)

"""
simple is the best 
"""

def evenOrOdd(num):
    if (num%2):
        return "Odd"
    else:
        return "Even"

#아래는 테스트로 출력해 보기 위한 코드입니다.
print("결과 : " + evenOrOdd(3))
print("결과 : " + evenOrOdd(2))