-- https://leetcode.com/problems/reported-posts/
-- Write your MySQL query statement below

-- 1. Filter rows based on yesterday's date and where action = 'report'
-- 2. Group by extra

SELECT
    extra AS report_reason,
    COUNT(DISTINCT post_id) AS report_count
FROM
    actions
WHERE
    action_date = DATE_ADD('2019-07-05', INTERVAL -1 DAY) AND action = 'report'
GROUP BY
    extra;
