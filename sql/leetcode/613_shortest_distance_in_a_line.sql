-- https://leetcode.com/problems/shortest-distance-in-a-line/

-- # Write your MySQL query statement below

SELECT MIN(ABS(p1.x - p2.x)) AS shortest
FROM Point p1
JOIN Point p2 ON p1.x != p2.x
