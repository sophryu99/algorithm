-- https://leetcode.com/problems/project-employees-ii/


# Write your MySQL query statement below
with cte AS (
    SELECT project_id, COUNT(employee_id) as cnt
    FROM Project
    GROUP BY project_id
)

SELECT project_id
FROM cte
WHERE cnt = (
    SELECT MAX(cnt)
    FROM cte
)