# https://leetcode.com/problems/kth-largest-element-in-a-stream/

"""
Uses basic minheap data structures
1. Create a heap with the input lists
2. Pop from the heap until heap.length == k
3. If length becomes larger than k, pop the smallest element from the heap
"""
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = nums
        heapq.heapify(self.heap)
        # Pop from the heap until heap.length == k
        while len(self.heap) > k:
            heapq.heappop(self.heap)
        

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        # If length becomes larger than k, pop the smallest element from the heap
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        # return the smallest element
        return self.heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

"""
Runtime: 159 ms, faster than 28.69% of Python3 online submissions for Kth Largest Element in a Stream.
Memory Usage: 18.2 MB, less than 92.76% of Python3 online submissions for Kth Largest Element in a Stream.
"""