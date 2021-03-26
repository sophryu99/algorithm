# https://www.acmicpc.net/problem/13423


def search(idx):
    global cnt

    if idx == 0 or idx == len(nums) - 1:
        return
    # search for nums[idx]
    for i in range(1, idx + 1):
        # locate left element
        left = nums[idx - i]
        # calculate the difference
        diff_left = abs(nums[idx] - left)
        for j in range(1, len(nums) - idx):
            # locate right element
            diff_right = abs(nums[idx] - nums[idx + j])
            if diff_right == diff_left:
                cnt += 1
                #print(left, nums[idx + j])
                #print(cnt)

T = int(input())

for tc in range(T):
    N = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    cnt = 0
    mid = len(nums) // 2
    # [-4, -1, 0, 2, 4]
    # [-4, 0, 4]
    # [-4, -1, 2]
    # [0, 2, 4]

    for i in range(1, len(nums) - 1):
        search(i)
    print(cnt)


            
