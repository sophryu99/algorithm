# https://www.acmicpc.net/problem/13423
import sys

T = int(sys.stdin.readline())

for tc in range(T):
    N = int(sys.stdin.readline())
    dots = list(map(int, sys.stdin.readline().split()))
    # [-4, -1, 0, 2, 4]
    dots.sort()

    cnt = 0
    for i in range(1, N):
        left = 0
        right = N - 1
        while right > left:
            #print('serach for', dots[i])
            leftDist = abs(dots[i] - dots[left])
            rightDist = abs(dots[i] - dots[right])
            #print('dots', dots[left], dots[right])
            #print('dist', leftDist, rightDist)

            if leftDist == rightDist:
                cnt += 1
                left += 1
            elif leftDist > rightDist:
                left += 1
            else:
                right -=1


    print(cnt)

            
