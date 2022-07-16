"""
#문제5
다음과 같이 n x n 크기의 격자에 1부터 n x n까지의 수가 하나씩 있습니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC1_qysbr6.png)
이때 수가 다음과 같은 순서로 배치되어있다면 이것을 n-소용돌이 수라고 부릅니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC2_ol8snc.png)
소용돌이 수에서 1행 1열부터 n 행 n 열까지 대각선상에 존재하는 수들의 합을 구해야 합니다.
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC3_cbcdg3.png)
위의 예에서 대각선상에 존재하는 수의 합은 15입니다.
격자의 크기 n이 주어질 때 n-소용돌이 수의 대각선상에 존재하는 수들의 합을 return 하도록 solution 함수를 완성해주세요.

---
##### 매개변수 설명
격자의 크기 n이 solution 함수의 매개변수로 주어집니다.

* n은 1 이상 100 이하의 자연수입니다.

---
##### return 값 설명
n-소용돌이 수의 대각선상에 존재하는 수들의 합을 return 해주세요.

---
##### 예시

| n 	| return 	|
|---	|--------	|
| 3 	| 15     	|
| 2 	| 4      	|

##### 예시 설명
예시 #1
문제의 예와 같습니다.

예시 #2
![image](http://res.cloudinary.com/sgc109/image/upload/c_scale,w_300/v1517462270/%EA%B7%B8%EB%A6%BC4_astq7q.png)
1과 3을 더하여 4가 됩니다.
"""


# You may use import as below.
# import math

def in_range(i,j,n):
    return 0 <= i and i < n and 0 <= j and j < n

def solution(n):
    pane = [[0 for j in range(n)] for i in range(n)]
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    ci, cj = 0, 0
    num = 1
    while in_range(ci, cj, n) and pane[ci][cj] == 0:
        for k in range(4):
            if not in_range(ci, cj, n) or pane[ci][cj] != 0:
                break
            while True:
                pane[ci][cj] = num
                num += 1
                ni = ci + dy[k]
                nj = cj + dx[k]
                if not in_range(ni, nj, n) or pane[ni][nj] != 0:
                    ci += dy[(k+1) % 4]
                    cj += dx[(k+1) % 4]
                    break
                ci = ni
                cj = nj
    # Write code here.
    answer = 0
    for i in range(n):
        answer += pane[i][i]
    return answer


# The following is code to output testcase.
n1 = 3
ret1 = solution(n1)

# Press Run button to receive output.
print("Solution: return value of the function is", ret1, ".")

n2 = 2
ret2 = solution(n2)

# Press Run button to receive output.
print("Solution: return value of the function is", ret2, ".")