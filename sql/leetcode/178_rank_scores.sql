-- https://leetcode.com/problems/rank-scores/

# Write your MySQL query statement below


SELECT score,
    DENSE_RANK() OVER(order by score desc) as `rank`
FROM (SELECT * FROM Scores Order by Score DESC) a