-- https://leetcode.com/problems/customers-who-bought-all-products/

# Write your MySQL query statement below

SELECT DISTINCT customer_id
FROM Customer
JOIN Product USING(product_key)
GROUP BY customer_id
HAVING COUNT(DISTINCT product_key) = (
    SELECT COUNT(product_key) FROM Product
)