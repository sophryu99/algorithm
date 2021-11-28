-- https://leetcode.com/problems/article-views-ii/

-- # Write your MySQL query statement below

-- # Group by viewer_id and view_date and aggregate by the count of the distinct article_id
-- # Filter group that has more than 1 count
-- # Order by id asc

SELECT DISTINCT viewer_id AS id
FROM Views
GROUP BY viewer_id, view_date
HAVING COUNT(DISTINCT article_id) > 1
ORDER BY id