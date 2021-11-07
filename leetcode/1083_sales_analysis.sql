-- https://leetcode.com/problems/sales-analysis-ii/
-- Write your MySQL query statement below

Input
-- Product
+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| product_id   | int     |
| product_name | varchar |
| unit_price   | int     |
+--------------+---------+

-- Sales
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| seller_id   | int     |
| product_id  | int     |
| buyer_id    | int     |
| sale_date   | date    |
| quantity    | int     |
| price       | int     |
+-------------+---------+

Output
+-------------+
| buyer_id    |
+-------------+
| 1           |
+-------------+

select distinct buyer_id
from Product p
join Sales s using(product_id)
where p.product_name='S8'
and s.buyer_id not in
(
    select distinct buyer_id
    from Product p
    join Sales s using(product_id)
    where p.product_name='iPhone'
)