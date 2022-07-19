"""
#문제8
1번부터 N번까지 후보에 대해서 투표를 진행했습니다. 예를 들어 투표 결과가 [1, 5, 4, 3, 2, 5, 2, 5, 5, 4]라면 순서대로 [1번, 5번, 4번, 3번, 2번, 5번, 2번, 5번, 5번, 4번] 후보에 투표했음을 나타냅니다. 이때, 가장 많은 표를 받은 후보의 번호를 구하려고 합니다.

주어진 solution 함수는 후보의 수 N과 투표를 진행한 결과가 담긴 리스트 votes가 매개변수로 주어졌을 때, 가장 많은 표를 받은 후보의 번호를 return 하는 함수입니다. 그러나, 코드 일부분이 잘못되어있기 때문에, 몇몇 입력에 대해서는 올바르게 동작하지 않습니다. 주어진 코드에서 _**한 줄**_만 변경해서 모든 입력에 대해 올바르게 동작하도록 수정하세요.

---
#####매개변수 설명
후보의 수 N과 투표 결과가 들어있는 리스트 votes가 solution 함수의 매개변수로 주어집니다.
* N은 1 이상 10 이하의 자연수입니다.
* votes의 길이는 1 이상 100 이하입니다.
* votes의 원소는 1 이상 N이하의 자연수입니다.

---
#####return 값 설명
가장 많은 표를 받은 후보의 번호를 리스트에 담아 return 해주세요
* 만약 가장 많은 표를 받은 후보가 2개 이상이라면, 그 후보들의 번호를 모두 리스트에 담아 오름차순 정렬하여 return 해주세요.

---
#####예시

| N | votes                 | return |
|---|-----------------------|--------|
| 5 | [1,5,4,3,2,5,2,5,5,4] | [5]    |
| 4 | [1,3,2,3,2]           | [2,3]  |

#####예시 설명
예시 #1
1번부터 5번까지 5개의 후보가 있으며, 투표 결과는 [1, 5, 4, 3, 2, 5, 2, 5, 5, 4]입니다. 각 후보의 득표수는 다음과 같습니다.

* 1번 후보가 1표
* 2번 후보가 2표
* 3번 후보가 1표
* 4번 후보가 2표
* 5번 후보가 4표

이 경우 5번 후보가 4표로 가장 많은 표를 얻었습니다.

예시 #2
1번 후보가 1표, 2번 후보가 2표, 3번 후보가 2표씩 받았습니다. 2번과 3번 후보가 공동으로 가장 많은 표를 받았기 때문에 [2, 3]을 오름차순 정렬하여 return 하면 됩니다.

"""


def solution(N, votes):
    vote_counter = [0 for i in range(N + 1)]
    for i in votes:
        vote_counter[i] += 1

    max_val = max(vote_counter)

    answer = []
    for idx in range(1, N + 1):
        if vote_counter[idx] == max_val:
            answer.append(idx)
    return answer


# The following is code to output testcase. The code below is correct and you shall correct solution function.
N1 = 5
votes1 = [1, 5, 4, 3, 2, 5, 2, 5, 5, 4]
ret1 = solution(N1, votes1)

# Press Run button to receive output.
print("Solution: return value of the function is ", ret1, " .")

N2 = 4
votes2 = [1, 3, 2, 3, 2]
ret2 = solution(N2, votes2)

# Press Run button to receive output.
print("Solution: return value of the function is ", ret2, " .")