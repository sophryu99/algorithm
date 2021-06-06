N, M = map(int, input().split())
workers = list(map(int, input().split()))     

time = 0
while M > 0:
    time += 1
    for i in range(len(workers)):
        # if time is divisible by worker's capacity
        if time % workers[i] == 0:
            M -= 1


print(time)
    



