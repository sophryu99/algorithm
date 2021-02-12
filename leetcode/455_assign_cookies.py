# https://leetcode.com/problems/assign-cookies/

"""
Approach:
1. Sort g, s as reverse order
2. Iterate through both lists, and increment count if g[i] <= s[j]
3. Remove s[j] from s as it is given to a child

Exception:
- If a cookie is given, it cannot be given to another child
- Sort both lists as reverse order to maximize the number of child who receives the cookie
"""

class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        count = 0
        g.sort(reverse = True)
        s.sort(reverse = True)
        for i in g:
            for j in s:
                if i <= j:
                    count += 1
                    s.pop(s.index(j))
                    break
                continue
        return count
                    
"""
Runtime: 744 ms, faster than 8.34% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.8 MB, less than 81.77% of Python3 online submissions for Assign Cookies.
"""
# As the runtime is very slow, I found a solution with faster runtime and less memory usage

-------------------

"""
Approach: 

"""
class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        res = 0
        g.sort(reverse=True)
        s.sort()
        for i in g:
            if not s: 
                return res
            elif i <= s[-1]:
                res += 1
                s.pop()
        return res

"""
Runtime: 156 ms, faster than 85.75% of Python3 online submissions for Assign Cookies.
Memory Usage: 15.8 MB, less than 92.04% of Python3 online submissions for Assign Cookies.
"""
