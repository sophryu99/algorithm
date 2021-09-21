# https://leetcode.com/problems/design-hashset/

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.sett = set()
        
    def add(self, key: int) -> None:
        self.sett.add(key)
        

    def remove(self, key: int) -> None:
        if key in self.sett:
            self.sett.remove(key)
        

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        if key in self.sett:
            return True
            
        


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)

"""
Runtime: 148 ms, faster than 87.79% of Python3 online submissions for Design HashSet.
Memory Usage: 19 MB, less than 53.85% of Python3 online submissions for Design HashSet.
"""