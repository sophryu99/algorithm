# https://programmers.co.kr/learn/courses/30/lessons/43165
# https://sophuu.tistory.com/84

# Brute Force
def solution(numbers, target):
    answer = 0
    # 1, -1
    current_list = [numbers[0], -numbers[0]]

    for i in range(1, len(numbers)):
        next_number = numbers[i]
        next_list = []
        for num in current_list:
            next_list.append(num + next_number)
            next_list.append(num - next_number)

        current_list = next_list

    for num in current_list:
        if num == target:
            answer += 1
    return answer


# DFS Approach
def solution(numbers, target):
    result = 0
    def dfs(num, level):
        nonlocal result

        if level == len(numbers):
            if num == target:
                result += 1
            return
        
        signs = [-num, num]
        if level == 1:
            for i in range(2):
                dfs(signs[i] + numbers[level], level + 1)
                dfs(signs[i] - numbers[level], level + 1)
        else:
            dfs(num + numbers[level], level + 1)
            dfs(num - numbers[level], level + 1)
                
    dfs(numbers[0], 1)
    return result