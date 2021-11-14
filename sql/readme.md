# SQL

## Concepts
CTE:
- A Common Table Expression, also called as CTE in short form, is a temporary named result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement.

What is a Relational Data Model? Explain Several Other Logical Data Models
- purpose of relations is to avoid data redundancy, ensure data integrity, and speed up data retrieval
- Every row is a single occurrence of the attributes. Rows are also called records.



## Codes
### Rouding up to 2 decimal points
```sql
ROUND(23.112342), 2)
>>> 23.11
```

### Rouding down to integer
```sql
SELECT FLOOR(your_field) FROM your_table
```

### Case when examples
```sql
SELECT x, y, z,
CASE 
    WHEN x = GREATEST(x, y, z) THEN (CASE WHEN x < y + z THEN 'Yes' ELSE 'No' END)
    WHEN y = GREATEST(x, y, z) THEN (CASE WHEN y < x + z THEN 'Yes' ELSE 'No' END)
    WHEN z = GREATEST(x, y, z) THEN (CASE WHEN z < x + y THEN 'Yes' ELSE 'No' END)
END As triangle
FROM Triangle
```

### Datetime between two datetimes
```sql
with cte as (
    SELECT p.product_id, SUM(units * prices) as revenue, sum(units) as quantity
    FROM Prices p
    JOIN UnitsSold u USING(product_id)
    WHERE purchase_date between start_date and end_date
)
```

### Getting the next date of curr date
```sql
DATE_ADD('2019-07-05', INTERVAL -1 DAY)
>>> '2019-07-04'
```

### Getting the greatest or least value amongst different columns
```sql
LEAST(c1,c2)
GREATEST(from_id,to_id)
```
### Getting string slices
```sql
SUBSTRING(phone_number,1,3)
```

### Using group by with case statement
```sql
SELECT stock_name,
    SUM(
        CASE
            WHEN operation = 'Buy' THEN -price
            ELSE price
        END
    )AS capital_gain_loss
FROM Stocks
GROUP BY stock_name
```

### Left join and fill null with 0
```sql
SELECT q.id, q.year, 
    (CASE WHEN n.npv IS NULL THEN 0 ELSE n.npv END) as npv
FROM Queries q
LEFT JOIN NPV n 
    ON q.id = n.id AND q.year = n.year

```

### Getting only date and month from datetime
```sql
DATE_FORMAT(pay_date,'%Y-%m') as pay_month
>>> DATE_FORMAT('2019/08/19', '%Y-%m')
>>> 2019-08
```