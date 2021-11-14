-- https://leetcode.com/problems/average-salary-departments-vs-company/

-- # Write your MySQL query statement below
-- # 1. create a cte with the salary by department and by each yearmonth
-- # 2. Self join cte with a grouped cte with the monthTotal salary per department
-- # 3. Join using the Yearmonth date and compare the monthTotal salary with the average salary by department

with cte as (
    SELECT department_id, pay_date, SUM(amount) as amount, COUNT(amount) as cnt
    FROM Salary
    JOIN Employee USING(employee_id)
    GROUP BY department_id, YEAR(pay_date), MONTH(pay_date)
)

SELECT DATE_FORMAT(cte.pay_date,'%Y-%m') as pay_month, department_id,
    (
    CASE 
        WHEN ROUND(monthTotal, 2) = ROUND(amount / cnt, 2) THEN 'same'
        WHEN monthTotal < amount / cnt THEN 'higher'
        ELSE 'lower'
     END
     ) AS comparison
FROM cte
JOIN (
    SELECT pay_date, 
        SUM(amount) / SUM(cnt) as monthTotal
    FROM cte
    GROUP BY YEAR(pay_date), MONTH(pay_date)
) AS temp ON DATE_FORMAT(temp.pay_date,'%Y-%m') = DATE_FORMAT(cte.pay_date,'%Y-%m')

