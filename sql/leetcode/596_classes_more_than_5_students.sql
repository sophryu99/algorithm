-- https://leetcode.com/problems/classes-more-than-5-students/

# Write your MySQL query statement below
with cte as (
    SELECT class, COUNT(student) as cnt
    FROM Courses
    GROUP BY class
    HAVING cnt >= 5
)

SELECT class FROM cte;

-- ----

SELECT
    class
FROM
    courses
GROUP BY class
HAVING COUNT(DISTINCT student) >= 5;