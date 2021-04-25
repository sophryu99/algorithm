# https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:    
        
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        diction = {}
        visited = []
        
        # store employee id and importance
        for info in employees:
            diction[info.id] = info.importance
            
        res = 0 
        for employee in employees:
            if employee.id == id:
                res += employee.importance
                if employee.subordinates:
                    for subs in employee.subordinates:
                        res += self.getImportance(employees, subs)
        return (res)

"""
Runtime: 328 ms, faster than 5.13% of Python3 online submissions for Employee Importance.
Memory Usage: 18.8 MB, less than 5.17% of Python3 online submissions for Employee Importance.
"""
