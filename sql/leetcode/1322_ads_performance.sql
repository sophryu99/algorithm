--  https://leetcode.com/problems/ads-performance/

-- # Write your MySQL query statement below
-- # ["ad_id", "ClickCount", "ViewCount"]
-- # [[1, 2, 1], 
-- #  [2, 1, 2], 
-- #  [3, 1, 1], 
-- #  [5, 0, 0]]
 

with cte AS (
    SELECT ad_id,
        SUM(CASE WHEN action = 'Clicked' THEN 1 ELSE 0 END) as clickCount,
        SUM(CASE WHEN action = 'Viewed' THEN 1 ELSE 0 END) as ViewCount
    FROM Ads
    GROUP BY ad_id
)

SELECT ad_id, 
CASE 
    WHEN ClickCount + ViewCount = 0 THEN 0.00
    ELSE ROUND(ClickCount / (ClickCount + ViewCount) * 100, 2)
END AS ctr
FROM cte
ORDER BY ctr DESC, ad_id ASC;
