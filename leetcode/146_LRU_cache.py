# https://leetcode.com/problems/lru-cache/

"""
Data structures with python
Get method: Return the value of the key if the key exists, otherwise return -1.
Put method: Update the value of the key if the key exists. Otherwise, add the key-value pair to the cache. If the number of keys exceeds the capacity from this operation, evict the least recently used key.
"""

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.count = 0
        
    def get(self, key: int) -> int:
        if key in self.cache:
            value = self.cache.pop(key)
            self.cache[key] = value
            return value
        return -1
        

    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            self.count += 1 #Increases the count of the total elements if a new one is added
        else:
            self.cache.pop(key) #Removes
        self.cache[key] = value #and adds/re-adds the element at the end since it is recently used
        if self.count > self.capacity:
            self.cache.pop(next(iter(self.cache))) #Removes the first dict item
            self.count -= 1
            
            
"""
["LRUCache", "put", "put", "get", "put", "get", "put", "get", "get", "get"]
[[2],        [1, 1], [2, 2], [1], [3, 3], [2], [4, 4], [1], [3], [4]]
[null,          null, null,   1,    null, -1,   null,   -1,  3,  4]


"""   
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)


"""
Runtime: 764 ms, faster than 81.90% of Python3 online submissions for LRU Cache.
Memory Usage: 75 MB, less than 52.46% of Python3 online submissions for LRU Cache.
"""