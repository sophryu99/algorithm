# Stack_4874_forth
# Forth에서는 동작은 다음과 같다.
 
# 숫자는 스택에 넣는다.
# 연산자를 만나면 스택의 숫자 두 개를 꺼내 더하고 결과를 다시 스택에 넣는다.
# ‘.’은 스택에서 숫자를 꺼내 출력한다.
# Forth 코드의 연산 결과를 출력하는 프로그램을 만드시오. 만약 형식이 잘못되어 연산이 불가능한 경우 ‘error’를 출력한다.
 

# [입력]
# 첫 줄에 테스트 케이스 개수 T가 주어진다.  1≤T≤50
# 다음 줄부터 테스트 케이스의 별로 정수와 연산자가 256자 이내의 연산코드가 주어진다. 피연산자와 연산자는 여백으로 구분되어 있으며, 코드는 ‘.’로 끝난다.
# 나눗셈의 경우 항상 나누어 떨어진다.


# [출력]
# #과 1번부터인 테스트케이스 번호, 빈칸에 이어 계산결과를 정수로 출력하거나 또는 ‘error’를 출력한다.

""" ---------- 내 풀이 (5/10 test case passed) ---------- """

# 접근: 입력 값에서 연산자가 아닌 경우에는 stack에 push 해준 후 연산자가 나오면 스택의 상위 두개의 원소를 pop 해준댜. 
# pop 해준 두 개의 원소를 연산자에 맞게 계산 해준 후 다시 스택에 push 해준다. 

op = {'+': lambda x, y: x + y,
      '*': lambda x, y: x * y,
      '-': lambda x, y: x - y,
      '/': lambda x, y: x / y}

T = int(input())
for i in range(T):
    stck = []
    operator = ['+', '*', '/', '-']
    lst = input().split()
    for l in range(len(lst)):
        if lst[l] not in operator:
            stck.append(lst[l])
        elif lst[l] in operator:
            if len(stck) > 1 :
                a = stck.pop()
                b = stck.pop()
                res = op[lst[l]](int(b),int(a))
                stck.append(res)
            else:
                stck.pop()
                stck.append('error')
    print('#{} {}'.format(i+1, stck[0]))
    

