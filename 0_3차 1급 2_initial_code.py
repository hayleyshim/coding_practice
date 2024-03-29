def func_a(arr, s): #arr에 s가 포함되어 있는지 확인 함수
    return s in arr

def func_b(s): # 부분 문자열(s)가 펠린드롬인지 비교
    length = len(s)
    for i in range(length // 2):
        if s[i] != s[length - i - 1]:
            return False
    return True

def func_c(palindromes, k): #리스트 길이 k 보다 작은지 비교, 팰린드롬에서 k번째 요소 반환
    palindromes = sorted(palindromes)
    if len(palindromes) < k:
        return "NULL"
    else:
        return palindromes[k - 1]

def solution(s, k): #문자열, k번째 큰 팰린트롬 찾을 변수
    palindromes = [] #펠린드롬 담을 리스트
    length = len(s) #문자열 길이
    for start_idx in range(length): #부분 문자열의 시작
        for cnt in range(1, length - start_idx + 1): 
            sub_s = s[start_idx : start_idx + cnt]
            if func_b(sub_s) == True: #펠린드롬인가? 
                if func_a(palindromes, sub_s) == False: #길이 비교
                    palindromes.append(sub_s)

    answer = func_c(palindromes, k)
    return answer


#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
s1 = "abcba"
k1 = 4
ret1 = solution(s1, k1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

s2 = "ccddcc"
k2 = 7
ret2 = solution(s2, k2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")