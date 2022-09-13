def func_a(arr): #arr 리스트 길이 2배 만들기
    ret = arr + arr
    return ret

def func_b(first, second): #회전했을 때 같은지 비교
    MAX_NUMBER = 1001
    counter = [0 for _ in range(MAX_NUMBER)]
    for f, s in zip(first, second):
        counter[f] += 1
        counter[s] -= 1
    for c in counter:
        if c != 0:
            return False
    return True

def func_c(first, second): #같은 리스트가 있는지 비교
    length = len(second)
    for i in range(length):
        if first[i : i + length] == second:
            return True
    return False

def solution(arrA, arrB):
    if len(arrA) != len(arrB): #길이가 같지 않으면 false return
        return False
    if func_b(arrA, arrB): #arrA 부분 리스트 중 arrB와 같은 리스트가 있으면 true, 그렇지않으면 false return
        arrA_temp = func_c(arrA, arrB)
        if func_a(arrA_temp):
            return True
    return False

#아래는 테스트케이스 출력을 해보기 위한 코드입니다. 
arrA1 = [1, 2, 3, 4]
arrB1 = [3, 4, 1, 2]
ret1 = solution(arrA1, arrB1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

arrA2 = [1, 2, 3, 4]
arrB2 = [1, 4, 2, 3]
ret2 = solution(arrA2, arrB2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")