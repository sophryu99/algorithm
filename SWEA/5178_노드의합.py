# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVJ-_6qfsDFAWg

def search(idx):
    idx = idx
    # add values to the parent node until it reaches the first node
    while idx > 1:
        node[idx//2] += node[idx]
        idx -=1


T = int(input())

for tc in range(T):
    N, M, L = map(int, input().split())
    node = [0] * (N + 1)
    for i in range(M):
        # add node values to each index
        idx, val = map(int, input().split())
        node[idx] = val
    
    # search from the last index
    search(N) 
    print("#{} {}".format(tc + 1, node[L]))
    

