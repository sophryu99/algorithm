-- https://leetcode.com/problems/find-the-team-size/

# Write your MySQL query statement below

with cte as (
    SELECT team_id, COUNT(employee_id) as team_size
    FROM Employee
    GROUP BY team_id
)

SELECT employee_id, team_size
FROM cte
JOIN Employee USING (team_id)