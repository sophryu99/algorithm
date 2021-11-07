-- https://leetcode.com/problems/triangle-judgement/

SELECT x, y, z,
CASE 
    WHEN x = GREATEST(x, y, z) THEN (CASE WHEN x < y + z THEN 'Yes' ELSE 'No' END)
    WHEN y = GREATEST(x, y, z) THEN (CASE WHEN y < x + z THEN 'Yes' ELSE 'No' END)
    WHEN z = GREATEST(x, y, z) THEN (CASE WHEN z < x + y THEN 'Yes' ELSE 'No' END)
END As triangle
FROM Triangle
           