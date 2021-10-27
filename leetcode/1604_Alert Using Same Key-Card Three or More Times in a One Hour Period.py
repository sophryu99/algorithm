# https://leetcode.com/problems/alert-using-same-key-card-three-or-more-times-in-a-one-hour-period/

import collections

class Solution:
    def alertNames(self, keyName: List[str], keyTime: List[str]) -> List[str]:
        check = collections.defaultdict(lambda: list())
        
        # Check if within an hour
        def calcdiff(start, end):
            time_diff = datetime.datetime.strptime(end, '%H:%M') - datetime.datetime.strptime(start, '%H:%M')
            minutes = int(time_diff.total_seconds()/60)
            return minutes <= 60
        
        # Add the timestamps to the dictionary
        for idx, name in enumerate(keyName):
            check[name].append(keyTime[idx])
            
        alert = []
        # Sort the timestamp lists per person
        for k, v in check.items():
            timesorted = sorted(v)
            for idx in range(len(timesorted) - 2):
                hour_later = datetime.datetime.strptime(timesorted[idx], '%H:%M')
                hour_later += timedelta(hours=1)
                cnt = 1
                for j in range(idx + 1, len(timesorted)):
                    currtime = datetime.datetime.strptime(timesorted[j], '%H:%M')
                    if currtime <= hour_later:
                        cnt += 1
                    if cnt == 3:
                        alert.append(k)
                        break
        
        return (sorted(list(set(alert))))

"""
Runtime: 2952 ms, faster than 5.29% of Python3 online submissions for Alert Using Same Key-Card Three or More Times in a One Hour Period.
Memory Usage: 38.3 MB, less than 88.50% of Python3 online submissions for Alert Using Same Key-Card Three or More Times in a One Hour Period.
Needs optimization
"""