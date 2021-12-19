# https://leetcode.com/discuss/interview-question/396769/
# Google OA 2019 - Intern

"""You are given a string that represents time in the format hh:mm. 
Some of the digits are blank (represented by ?). 
Fill in ? such that the time represented by this string is the maximum possible. 
Maximum time: 23:59, minimum time: 00:00. You can assume that input string is always valid.
"""

time = str(input())

arr = list(time)

for i in range(len(arr)):
    if arr[i] == '?':
        # First digit
        if i == 1:
            if arr[2] == '?':
                arr[i] = '2'
            else:
                if int(arr[2]) >= 4:
                    arr[i] = '1'
                elif int(arr[2]) < 4:
                    arr[i] = '2'
        # Second digit
        elif i == 2:
            if int(arr[1]) == 1 or int(arr[1]) == 0:
                arr[i] = '9'
            elif int(arr[1]) == 2:
                arr[i] = '3'
        elif i == 4:
            arr[i] = '5'
        else:
            arr[i] = '9'

print(''.join(arr))


