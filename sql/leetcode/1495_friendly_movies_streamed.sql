-- https://leetcode.com/problems/friendly-movies-streamed-last-month/

-- # Write your MySQL query statement below


SELECT DISTINCT title
FROM TVProgram
JOIN Content USING(content_id)
WHERE Kids_content = 'Y' 
AND MONTH(program_date) = 6 
AND YEAR(program_date) = 2020
AND content_type = 'Movies'

