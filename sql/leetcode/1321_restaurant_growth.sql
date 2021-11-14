-- https://leetcode.com/problems/restaurant-growth/


SELECT a.visited_on AS visited_on, SUM(b.day_sum) AS amount,
       ROUND(AVG(b.day_sum), 2) AS average_amount
FROM
  (SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on ) a,
  (SELECT visited_on, SUM(amount) AS day_sum FROM Customer GROUP BY visited_on ) b
WHERE DATEDIFF(a.visited_on, b.visited_on) BETWEEN 0 AND 6 # To make sure the rolling sum and rolling avg are only calculated in a 7-day window 
GROUP BY a.visited_on
HAVING COUNT(b.visited_on) = 7 # This is to make sure it starts from the 7th day since only if it reaches the 7th day there will be 7 days that are 0-6 days
# prior to the current days (e.g. for the first day, there's only itself that is 0-6 days prior to itself; and for the second day it's itself and the day prior, etc.,).