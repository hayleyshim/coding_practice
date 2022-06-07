"""
문제 설명

길이가 n이고, "수박수박수박수...."와 같은 패턴을 유지하는 문자열을 리턴하는 함수, solution을 완성하세요. 예를들어 n이 4이면 "수박수박"을 리턴하고 3이라면 "수박수"를 리턴하면 됩니다.
제한 조건

- n은 길이 10,000이하인 자연수입니다.
입출력 예

n
return
3
"수박수"
4
"수박수박"

"""

def solution(n):
    answer = ''

    if n % 2 == 0:
        answer += '수박' * (n // 2)
        return answer
    else:
        answer += '수박' * (n // 2) + '수'
        return answer

print(solution(3))
print(solution(4))


def water_melon(n):
    s = "수박" * n
    return s[:n]


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));


def water_melon(n):
    return "수박"*(n//2) + "수"*(n%2)


# 실행을 위한 테스트코드입니다.
print("n이 3인 경우: " + water_melon(3));
print("n이 4인 경우: " + water_melon(4));

