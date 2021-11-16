-- https://leetcode.com/problems/find-the-missing-ids/

-- # Write your MySQL query statement below

-- # 1. Create a cte that contains 1 - max(val) id
-- # 2. Check for the ids that are not in the customers table

with recursive rnums as (
  select 1 as ids
      union all
  select ids + 1 as ids from rnums
      where ids < (SELECT max(customer_id) FROM customers)
)
  
select ids
from rnums
WHERE ids NOT IN (SELECT customer_id FROM customers)

