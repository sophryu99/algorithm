-- https://leetcode.com/problems/list-the-products-ordered-in-a-period/

-- # Write your MySQL query statement below
-- # 1. Filter Orders table Feb 2020
-- # 2. Join orders, products
-- # 3. Group the oarders

SELECT product_name, unit
FROM Products
JOIN (
    SELECT product_id, SUM(unit) as unit
    FROM Orders
    WHERE Year(order_date) = 2020 AND Month(order_date) = 2
    GROUP BY product_id
    HAVING unit >= 100
) AS temp USING(product_id)



