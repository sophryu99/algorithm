# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # 1. Locate peaks
    peaks = []
    for order in range(1, len(A) - 1):
        current = A[order]
        if current >= A[order - 1] and current >= A[order + 1]:
            peaks.append(order)

    print(peaks)
    maxcnt = 1
    k = 2
    left = 0
    right = left + 1
    while k <= len(peaks):
        # for i in range(len(peaks) - 2):
        #     flags = [0] * len(peaks)
        #     for j in range(i + 1, len(peaks) - 1):
        #         if abs(peaks[i] - peaks[j]) >= k: 
        
        for i in range(len(peaks)):
            if abs(peaks[left] - peaks[right]):
                return 2

        


        
        k += 1



    """
    1 -> 3 : 2
    1 -> 5 : 4
    1 -> 10 : 9

    3 -> 5: 2
    3 -> 10: 7

    5 -> 10: 5

    """




