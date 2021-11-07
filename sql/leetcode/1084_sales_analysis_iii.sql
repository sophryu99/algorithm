-- https://leetcode.com/problems/sales-analysis-iii/

-- # Write your MySQL query statement below
-- # Logic:
-- # 1. Create a table where it contains rows within Spring 2019 and another table outside of Spring 2019
-- # 2. Return product_id and product_name which is in the first table but not in the second

SELECT DISTINCT product_id, product_name
FROM Sales 
JOIN Product USING(product_id)
WHERE product_id IN
(
    SELECT product_id
    FROM Sales
    WHERE sale_date >= '2019-01-01' AND sale_date <= '2019-03-31')
AND product_id NOT IN
(
    SELECT product_id
    FROM Sales
    WHERE sale_date < '2019-01-01' OR sale_date > '2019-03-31'
)