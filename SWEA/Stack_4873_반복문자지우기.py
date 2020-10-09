# 4873 반복문 지우기

# [문제]
# 문자열 s에서 반복된 문자를 지우려고 한다. 지워진 부분은 다시 앞뒤를 연결하는데, 만약 연결에 의해 또 반복문자가 생기면 이부분을 다시 지운다.
# 반복문자를 지운 후 남은 문자열의 길이를 출력 하시오. 남은 문자열이 없으면 0을 출력한다.

# 다음은 CAAABBA에서 반복문자를 지우는 경우의 예이다.
# CAAABBA 연속 문자 AA를 지우고 C와 A를 잇는다.
# CABBA 연속 문자 BB를 지우고 A와 A를 잇는다.
# CAA 연속 문자 AA를 지운다.
# C 1글자가 남았으므로 1을 리턴한다.


""" ---------- 내 풀이 (pass) ---------- """

# 접근: 스트링의 값들을 stack에 순서대로 append 해준 후 스택의 가장 상위 부분에 같은 스트링 값이 있는 경우는 pop 해준다.

T = int(input())
for i in range(T):
    lst = input()
    stack = []
    for l in range(len(lst)):
        if len(stack) == 0:                       # stack이 비어있을 때는 입력 값을 append 해준다
            stack.append(lst[l])
        elif stack[-1] != lst[l]:                 # stack의 가장 위의 스트링 값이 입력 값과 같지 않을 때
            stack.append(lst[l])                  # 입력 값을 스택에 append 해준다
        elif stack[-1] == lst[l]:                 # stack의 가장 위의 스트링 값이 입력 값과 일치 할 때
            stack.pop()                           # 해당 값을 stack에서 제거해준다.
    print('#{} {}'.format(i+1, len(stack)))

    