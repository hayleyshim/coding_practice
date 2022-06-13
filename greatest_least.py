def gcd(n,m):
    mod = m % n
    if mod != 0:
        m, n = n, mod
        return gcd(n,m)
    else:
        return n

def solution(n,m):
    return(gcd(n,m), int(m*n/gcd(n,m)))

print(solution(3,12))
print(solution(2,5))


def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
    answer = [c, int(a*b/c)]

    return answer

# 아래는 테스트로 출력해 보기 위한 코드입니다.
print(gcdlcm(3,12))


