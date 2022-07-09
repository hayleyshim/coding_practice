"""
스택으로 큐 구현
문제 설명
스택 두개를 이용해 Queue 자료구조를 만들었을 때, Queue 자료 구조의 pop(또는 dequeue) 함수를 구현하려합니다. Queue란 먼저 삽입한 데이터를 먼저 빼내는 자료구조를 뜻합니다. pop 함수를 만들기 위해 다음과 같이 프로그램 구조를 작성했습니다.

1. 스택2가 비었다면 스택1에 아무것도 남지 않을때까지 스택1에서 pop한 값을 스택2에 push 한다.
2. 스택2에서 pop한 값을 리턴한다.
두 리스트 stack1, stack2가 매개변수로 주어질 때, 두 리스트를 스택으로 이용해 Queue 자료 구조의 pop 함수를 구현하려합니다. 위 구조를 참고하여 코드가 올바르게 동작할 수 있도록 빈칸에 주어진 func_a, func_b, func_c 함수와 매개변수를 알맞게 채워주세요.

※ 리스트 index가 0인 부분을 스택의 bottom으로 생각합니다.

매개변수 설명
두 리스트 stack1와 stack2가 solution 함수의 매개변수로 주어집니다.

stack1과 stack2는 길이가 0 이상 10 이하입니다.
stack1과 stack2의 길이가 모두 0인 경우는 주어지지 않습니다.
stack1과 stack2의 원소는 100 이하인 정수입니다.
return 값 설명
stack1과 stack2로 구현한 큐에서 pop(또는 dequeue)한 값을 return 해주세요.

"""

def func_a(stack):
    return stack.pop()

def func_b(stack1, stack2):
    while not func_c(stack1):
        item = func_a(stack1)
        stack2.append(item)

def func_c(stack):
    return (len(stack) == 0)

def solution(stack1, stack2):
    if func_c(stack2):
        func_b(stack1, stack2)

    answer = func_a(stack2)
    return answer

# 아래는 테스트케이스 출력을 해보기 위한 코드입니다.
stack1_1 = [1,2]
stack2_1 = [3,4]
ret1 = solution(stack1_1, stack2_1)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

stack1_2 = [1,2,3]
stack2_2 = []
ret2 = solution(stack1_2, stack2_2)

# [실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")

"""
Stack은 선입후출, First in Last out 방식이고, Queue는 선입선출, First in First Out 방식입니다.

따라서 Stack으로 Queue를 구현하려면, 두 개의 Stack을 사용하여 옮겨담는 과정이 필요합니다.

func_a는 Stack의 맨 위의 원소를 pop하여 return하는 함수입니다.

func_b는 stack1의 값을 빈 stack2에 옮겨담는 함수입니다.

func_c는 stack이 비어있는지 확인하는 함수입니다.

따라서, 문제에 주어진 조건대로 stack2가 비어있는지 확인 한 이후에

stack1의 원소들을 stack2에 모두 옮겨담은 후

stack2에서 pop하게 되면 가장 먼저 저장된 값이 가장 아래로 내려가게 되어 FILO를 완성할 수 있습니다.
"""