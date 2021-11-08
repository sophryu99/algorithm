-- https://leetcode.com/problems/customer-placing-the-largest-number-of-orders/

# Write your MySQL query statement below
with cte as(
    SELECT customer_number, COUNT(order_number) as order_count
    FROM Orders
    GROUP BY customer_number
)

SELECT customer_number
FROM cte
WHERE order_count = (
    SELECT MAX(order_count)
    FROM cte
)