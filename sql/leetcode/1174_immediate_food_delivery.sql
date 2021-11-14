-- https://leetcode.com/problems/immediate-food-delivery-ii/
-- # Write your MySQL query statement below

SELECT ROUND(
    (
        SELECT SUM(
            CASE 
                WHEN order_date = customer_pref_delivery_date THEN 1
                ELSE 0
            END
    )) / COUNT(DISTINCT customer_id) * 100, 2) as immediate_percentage
FROM Delivery
WHERE (customer_id, order_date) IN
    (SELECT DISTINCT customer_id, MIN(order_date) as order_date
     FROM Delivery
     GROUP BY customer_id
    )