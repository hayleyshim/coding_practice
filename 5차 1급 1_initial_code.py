def solution(n):
	answer = 0
	steps = [0 for _ in range(n+1)]
	print(steps)
	steps[1] = 1
	steps[2] = 2
	steps[3] = 4
	for i in range(4, n+1):
		steps[i] = @@@
	answer = steps[n]steps
	return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
ret1 = solution(n1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 4
ret2 = solution(n2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")