# https://www.acmicpc.net/problem/4889


tc = 0
while True:
    stack = []
    tc += 1
    s = list(input())
    if '-' in s:
        break

    count = 0

    for i in range(len(s)):
        if s[i] == '{':
            stack.append(s[i])

        elif s[i] == '}':
            if len(stack) == 0:
                stack.append('{')
                count += 1
            else:
                stack.pop()
    
    print('{}. {}'.format(tc, len(stack) // 2 + count))