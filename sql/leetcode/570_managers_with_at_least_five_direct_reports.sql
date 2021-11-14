-- https://leetcode.com/problems/managers-with-at-least-5-direct-reports/

-- # Write your MySQL query statement below
-- # 1. Group by the count for each managerId and filter rows with at least 5 counts
-- # 2. Inner join cte with the employee table

with cte as (
    SELECT managerId, COUNT(*) as report
    FROM Employee
    GROUP BY managerId
    HAVING report >= 5
)

SELECT DISTINCT name
FROM Employee e
JOIN cte c ON e.id = c.managerId

