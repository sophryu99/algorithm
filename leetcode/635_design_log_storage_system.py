# https://leetcode.com/problems/design-log-storage-system/

class LogSystem:

    def __init__(self):
        self.logsystem = []
        
    def put(self, id: int, timestamp: str) -> None:
        self.logsystem.append((timestamp, id))
        self.logsystem = sorted(self.logsystem)
        

    def retrieve(self, start: str, end: str, granularity: str) -> List[int]:
        ans = []
        
        gran_dict = {'Year': 4, 'Month':7, 'Day': 10, 'Hour': 13, 'Minute': 16, 'Second':19}
        parsed_start = start[:gran_dict[granularity]]
        parsed_end = end[:gran_dict[granularity]]
        
        for time in self.logsystem:
            print(time[0][:gran_dict[granularity]])
            if (time[0][:gran_dict[granularity]] >= parsed_start) and (time[0][:gran_dict[granularity]] <= parsed_end):
                ans.append(time[1])
        
        return ans
            

# Your LogSystem object will be instantiated and called as such:
# obj = LogSystem()
# obj.put(id,timestamp)
# param_2 = obj.retrieve(start,end,granularity)

"""
Runtime: 123 ms, faster than 5.31% of Python3 online submissions for Design Log Storage System.
Memory Usage: 14.6 MB, less than 40.61% of Python3 online submissions for Design Log Storage System.
"""
