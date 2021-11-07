# SQL

## Concepts
CTE:
- A Common Table Expression, also called as CTE in short form, is a temporary named result set that you can reference within a SELECT, INSERT, UPDATE, or DELETE statement.

What is a Relational Data Model? Explain Several Other Logical Data Models
- purpose of relations is to avoid data redundancy, ensure data integrity, and speed up data retrieval
- Every row is a single occurrence of the attributes. Rows are also called records.



## Codes
Rouding up to 2 decimal points
```sql
ROUND(23.112342), 2)
>>> 23.11
```

Rouding down to integer
```sql
SELECT FLOOR(your_field) FROM your_table
```

Case when examples
```sql
SELECT x, y, z,
CASE 
    WHEN x = GREATEST(x, y, z) THEN (CASE WHEN x < y + z THEN 'Yes' ELSE 'No' END)
    WHEN y = GREATEST(x, y, z) THEN (CASE WHEN y < x + z THEN 'Yes' ELSE 'No' END)
    WHEN z = GREATEST(x, y, z) THEN (CASE WHEN z < x + y THEN 'Yes' ELSE 'No' END)
END As triangle
FROM Triangle
```