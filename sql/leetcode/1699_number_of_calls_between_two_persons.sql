-- https://leetcode.com/problems/number-of-calls-between-two-persons/


-- # Write your MySQL query statement below

SELECT LEAST(from_id,to_id) as person1,
GREATEST(from_id,to_id) as person2,
COUNT(*) as call_count,
SUM(duration) as total_duration
FROM Calls
GROUP BY person1, person2;