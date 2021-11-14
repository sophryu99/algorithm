-- https://leetcode.com/problems/npv-queries/

-- # Write your MySQL query statement below

SELECT q.id, q.year, 
    (CASE WHEN n.npv IS NULL THEN 0 ELSE n.npv END) as npv
FROM Queries q
LEFT JOIN NPV n 
    ON q.id = n.id AND q.year = n.year
