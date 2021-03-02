# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AV184o76I7sCFAZN

"""
Approach: dfs
SWEA D4
"""
def dfs(vertex):
    global res
    # if reached end
    if vertex == 99:
        res = 1
        return

    for i in range(len(new)):
        # get the next eleme for the vertex
        if new[i][0] == vertex and not visited[new[i][0]]:
            visited[new[i][0]] = 1
            #print(visited)
            # print(new[i][0], '->', new[i][1])
            dfs(new[i][1])
            visited[new[i][0]] = 0
    
    #print(visited)
for tc in range(10):
    T, N = map(int, input().split())

    l = list(map(int, input().split()))
    # create a list containing connected vertex
    new = list(zip(l[::2], l[1::2]))
    res = 0
    # for each num
    visited = [0] * 100
    dfs(0)
    print("#{} {}".format(T, res))
        