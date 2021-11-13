-- https://leetcode.com/problems/tree-node/

-- # Write your MySQL query statement below

-- # Judge the node type by checking if the node's id shows up in p_id columm and whether the node's p_id is null
-- # If p_id is null, p_id is root
-- # If id shows up in p_id, Inner
-- # IF id does not show up p_id, Leaf

SELECT id, 
    CASE 
        WHEN p_id IS NULL THEN 'Root'
        WHEN id IN (SELECT p_id FROM Tree) THEN 'Inner'
        ELSE 'Leaf'
    END AS type
FROM tree
ORDER BY id