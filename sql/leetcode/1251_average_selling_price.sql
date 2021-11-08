-- https://leetcode.com/problems/average-selling-price/

-- # Write your MySQL query statement below
-- # 1. Calculate the total revenue of products by joining on condition where the purchase date is within the start and the end date
-- # 2. Return the average price by dividing the revenue with quantity and rouding up to 2 decimal points

with cte as (
    SELECT p.product_id, SUM(units * price) as revenue, sum(units) as quantity
    FROM Prices p
    JOIN UnitsSold u USING(product_id)
    WHERE purchase_date between start_date and end_date
    GROUP BY p.product_id
)

SELECT product_id, ROUND(revenue / quantity, 2) AS average_price
FROM cte
