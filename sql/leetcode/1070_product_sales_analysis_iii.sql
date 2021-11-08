-- https://leetcode.com/problems/product-sales-analysis-iii/

# Write your MySQL query statement below

with cte AS (
    SELECT product_id, MIN(year) as first_year
    FROM Sales
    GROUP BY product_id
)

SELECT s1.product_id, s1.first_year, s2.quantity, s2.price
FROM cte s1
INNER JOIN Sales s2 ON s1.product_id = s2.product_id AND s1.first_year = s2.year
