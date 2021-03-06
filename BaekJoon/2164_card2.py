# 문제: 2164
# N장의 카드가 있다. 각각의 카드는 차례로 1부터 N까지의 번호가 붙어 있으며, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있다.
# 이제 다음과 같은 동작을 카드가 한 장 남을 때까지 반복하게 된다. 우선, 제일 위에 있는 카드를 바닥에 버린다. 그 다음, 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.
# 예를 들어 N=4인 경우를 생각해 보자. 카드는 제일 위에서부터 1234 의 순서로 놓여있다. 1을 버리면 234가 남는다. 여기서 2를 제일 아래로 옮기면 342가 된다. 3을 버리면 42가 되고, 4를 밑으로 옮기면 24가 된다. 마지막으로 2를 버리고 나면, 남는 카드는 4가 된다.

# N이 주어졌을 때, 제일 마지막에 남게 되는 카드를 구하는 프로그램을 작성하시오.

# 입력
# 첫째 줄에 정수 N(1≤N≤500,000)이 주어진다.

# 출력
# 첫째 줄에 남게 되는 카드의 번호를 출력한다.

""" ---------- 내 풀이 (첫 시도: 시간초과) ---------- """

# 접근: 1~N 까지의 수를 스택에 append 한다. for loop이 한번 돌 때 스택의 가장 위의 원소를 pop해주고 그 다음 원소의 인덱스를 재설정 해준다.
# 스택의 가장 밑에 위치하도록 원소의 인덱스를 재설정해주고 그에 따라 다른 원소들의 인덱스 역시 재설정 해주는것이 관건이다.
# 접근 수정: 스택의 가장 하위에 새로운 원소를 추가하는 것이 어려워 애초에 스택에 입력 값을 역순으로 넣어주었다.
# lst = [1, 2, 3, 4]
# lst.pop(0)-> x = lst[0].pop -> lst.append(lst[0])


# N = int(input())
# stack = []
# for i in range(N):
#     stack.append(i+1)           # 입력 역순으로 스택에 push 해주기
# while len(stack) > 1:           # 스택이 비어있지 않을 때
#     stack.pop(0)                # 가장 하위 인자 pop
#     top = stack.pop(0)          # 그 다음 하위 인자를 변수에 저장 후
#     stack.append(top)           # 스택의 가장 상위에 append 해준다.
# print(stack[0])


""" ---------- deque를 사용한 풀이 (pass) ---------- """

from collections import deque 

N = int(input()) 
queue = deque() 
for i in range(N): 
    queue.append(i + 1) 
    
while len(queue) > 1: 
    queue.popleft() 
    queue.append(queue.popleft()) 
print(queue.pop())
