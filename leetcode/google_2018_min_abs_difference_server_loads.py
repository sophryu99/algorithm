# https://leetcode.com/discuss/interview-question/356433/

"""
There are some processes that need to be executed. 
Amount of a load that process causes on a server that runs it, is being represented by a single integer. 
Total load caused on a server is the sum of the loads of all the processes that run on that server. 
You have at your disposal two servers, on which mentioned processes can be run. 
Your goal is to distribute given processes between those two servers in the way that, absolute difference of their loads will be minimized.

Given an array of n integers, of which represents loads caused by successive processes, return the minimum absolute difference of server loads."""

"""
Input: [1, 2, 3, 4, 5]
Output: 1
Explanation:
We can distribute the processes with loads [1, 2, 4] to the first server and [3, 5] to the second one,
so that their total loads will be 7 and 8, respectively, and the difference of their loads will be equal to 1.

"""
"""
My Approach:
1. Solve for the sum of the total loads (T)
2. Create a dp table with the subset of the array stored
3. Compare for the least differences
"""

def subsetsUtil(A, subset, index):
    for i in range(index, len(A)): 
          
        # include the A[i] in subset. 
        subset.append(A[i])
          
        # move onto the next element. 
        subsetsUtil(A, subset, i + 1) 
          
        # exclude the A[i] from subset and 
        # triggers backtracking.
        subset.pop(-1) 
    return
def subsets(A):
    global res
    subset = []
      
    # keeps track of current element in vector A 
    index = 0
    subsetsUtil(A, subset, index) 

def distribute(lst):
    totalsum = sum(lst) // 2 + 1
    dp = [[0 for i in range(totalsum)] for j in range(len(lst) + 1)]
    #print(dp)
    # for idx, item in enumerate(lst):
    #     print(idx, item)
    for i in range(len(lst) + 1 ):
        dp[i][0] = True
    
    for i in range(1, totalsum + 1):
        dp[0][i]= False

    for i in range(1, len(lst) + 1 ):
        for j in range(1, totalsum + 1):
            if j < [i-1]:
                subset[i][j] = subset[i-1][j]
            if j>= set[i-1]:
                subset[i][j] = (subset[i-1][j] or
                                subset[i - 1][j-set[i-1]])





print(distribute([1,2,3,4,5]))


