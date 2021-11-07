https://leetcode.com/problems/sales-analysis-i/

-- My Attempt
with cte AS (
    SELECT s.seller_id, SUM(p.unit_price * s.quantity) AS revenue
    FROM Product p
    JOIN Sales s USING(product_id)
    GROUP BY s.seller_id
)

SELECT seller_id
FROM cte 
WHERE revenue = (
    SELECT MAX(revenue) 
    FROM cte
)