# 주어진 입력에서 괄호 {}, ()가 제대로 짝을 이뤘는지 검사하는 프로그램을 만드시오.
# 예를 들어 {( )}는 제대로 된 짝이지만, {( })는 제대로 된 짝이 아니다. 입력은 한 줄의 파이썬 코드일수도 있고, 괄호만 주어질 수도 있다.
# 정상적으로 짝을 이룬 경우 1, 그렇지 않으면 0을 출력한다.
# print(‘{‘) 같은 경우는 입력으로 주어지지 않으므로 고려하지 않아도 된다.


# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스 별로 온전한 형태이거나 괄호만 남긴 한 줄의 코드가 주어진다.

# [출력]
# 각 줄마다 "#T" (T는 테스트 케이스 번호)를 출력한 뒤, 답을 출력한다.

""" ---------- 내 풀이 (pass: 0.13988s) ---------- 
    시도 1: runtime error
    시도 2: pass
"""

""" 접근: 입력값을 string으로 받고 입력값의 길이 안에서 괄호 탐색 실시 
    여는 괄호 "(" 발견 시 스택에 push 해줌
    닫는 괄호 ")" 발견 시 스택에 존재하는 여는 괄호 "("를 꺼내준다
    최종적으로 스택의 길이가 0이면 1을 리턴해준다
"""

# 시도 2: pass
T = int(input())
for t in range(T):
    Data = input()
    stack = []
    result = 0 
    for i in range(len(Data)):
        if Data[i] == "(" or Data[i] == "{":                        # 여는괄호가 올 경우 stack에 push
            stack.append(Data[i])
        elif Data[i] == ")" or Data[i] == "}":                      # 닫는괄호 이며 stack이 빈 경우
            if len(stack) == 0:                                     # 처음부터 닫는 괄호가 오는 경우 (스택이 빈 경우)
                stack = [Data[i]]
                break                                               # 입력된 괄호와 stack의 top에 있는 괄호와 일치하지 않는 경우
            elif (Data[i] == "}" and stack[-1] !="{") or (Data[i] == ")" and stack[-1] != "("):  
                stack = [Data[i]]
                break
            else:                                                   #stack에 저장된 괄호와 일치하는 닫는 괄호가 오는 경우
                stack.pop()
    
    if len(stack) == 0:
        result = 1
    else:
        result = 0
    print("#{} {}".format(i+1, result))


"""
시도 1 (runtime error: 몇가지의 경우에 따른 예외처리를 안해줌)
T = int(input())
for i in range(T):
    stack = []
    result = 0
    N = list(map(str, input()))                 # 입력값 스트링으로 받아주기
    for n in range(len(N)):                     # 입력값 각각의 element 별로 탐색 실시
        if N[n] == '(' or N[n] == '{':          # {, ( 발견시 스택에 푸쉬
            stack.append(N[n])
        elif N[n] == ')' or N[n] == '}':          # }, ) 발견시 스택의 가장 위에 있는 괄호 pop
            stack.pop()
    if len(stack) == 0:                         # stack의 길이가 0이면 1 리턴, 아닐시 0 리턴
        result = 1
    else:
        result = 0
    print("#{} {}".format(i+1, result)) 
    """

        