# https://leetcode.com/problems/design-hashmap/

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.mapp = {}
        
    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        # If the value is not in the hashmap, add correspoding values
        self.mapp[key] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        if key in self.mapp:
            return self.mapp[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.mapp:
            self.mapp.pop(key)
        
        


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

"""
Runtime: 192 ms, faster than 97.40% of Python3 online submissions for Design HashMap.
Memory Usage: 17.2 MB, less than 90.29% of Python3 online submissions for Design HashMap.
"""