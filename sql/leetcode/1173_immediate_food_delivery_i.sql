-- https://leetcode.com/problems/immediate-food-delivery-i/


-- # Write your MySQL query statement below

-- # 1. Get the total count of the table
-- # 2. Find rows where immediate_delivery = order_date
-- # 3. Divide immediate_delivery count / total count

with cte as (
    SELECT COUNT(*) as order_count
    FROM Delivery
    WHERE customer_pref_delivery_date = order_date
)

SELECT ROUND((
    SELECT order_count
    FROM cte
) / COUNT(*) * 100, 2) as immediate_percentage 
FROM Delivery
