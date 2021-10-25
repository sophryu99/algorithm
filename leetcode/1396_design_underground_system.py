# https://leetcode.com/problems/design-underground-system/submissions/

import collections
class UndergroundSystem:

    def __init__(self):
        self.check_in_data = {}
        self.journey_data = collections.defaultdict(lambda : [0, 0])
                
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in_data[id] = [stationName, t]

    def checkOut(self, id: int, end_station: str, t: int) -> None:
        start_station, start_time = self.check_in_data.pop(id)
        self.journey_data[(start_station, end_station)][0] += (t - start_time)
        self.journey_data[(start_station, end_station)][1] += 1
            
    def getAverageTime(self, start_station: str, end_station: str) -> float:
        total_time, total_trips = self.journey_data[(start_station, end_station)]
        return total_time / total_trips

"""
Runtime: 298 ms, faster than 41.75% of Python3 online submissions for Design Underground System.
Memory Usage: 24 MB, less than 88.62% of Python3 online submissions for Design Underground System.

"""