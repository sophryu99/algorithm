#https://leetcode.com/problems/meeting-rooms-ii/

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0
        
        # Sort the array according to the start time
        intervals.sort(key = lambda x: x[0])
        
        # Initialize heap and add the first meeting
        rooms = []
        heapq.heappush(rooms, intervals[0][1])
    
        for i in intervals[1:]:
            # If the room is free, assign the room to this meeting
            if rooms[0] <= i[0]:
                heapq.heappop(rooms)
                
            
            # Add the next meeting's end time to the heap
            heapq.heappush(rooms, i[1])
        
        return (len(rooms))
        
        
        
"""
Runtime: 80 ms, faster than 66.11% of Python3 online submissions for Meeting Rooms II.
Memory Usage: 17.3 MB, less than 98.63% of Python3 online submissions for Meeting Rooms II.
"""