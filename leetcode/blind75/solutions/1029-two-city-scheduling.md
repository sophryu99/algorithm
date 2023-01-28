# https://leetcode.com/problems/two-city-scheduling/description/

# Approach
<!-- Describe your approach to solving the problem. -->
- Send everyone to the first city first, and send the half to the other city which has the least difference between the costs

For example `costs = [[10,20],[30,200],[400,50],[30,20]]` :
1. Send everyone to the first city which sums to `10 + 30 + 400 + 30 = 470`.
2. Calculate the difference between the cost, `10, 170, -350, -10`
3. Sort the difference and get the cost that has the minimum differences (this means refund)
4. Evaluate `10 + 30 + 400 + 30 + (-350 -10)`

# Complexity
- Time complexity:  `O(nlog(n))` -> sort()
- Space complexity: `O(n)`

# Code
```python3
"""
Send everyone to the first city first, and send the half to the other city
which has the least difference between the costs
"""

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        totalsum = 0
        for i, cost in enumerate(costs):
            diff.append(cost[1] - cost[0])
            totalsum += cost[0]

        # sort by the differences
        diff.sort()
        for i in range(len(costs) // 2):
            totalsum += diff[i]
        return (totalsum)









```
