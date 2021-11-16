-- https://leetcode.com/problems/movie-rating/

-- # Write your MySQL query statement below

(SELECT name as results
FROM Users
JOIN MovieRating USING(user_id)
GROUP BY user_id
ORDER BY COUNT(movie_id) DESC, name ASC
LIMIT 1)
UNION (
SELECT title
FROM MovieRating
JOIN Movies USING(movie_id)
WHERE MONTH(created_at) = 2 AND YEAR(created_at) = 2020
GROUP BY movie_id
ORDER BY AVG(rating) DESC, title ASC
LIMIT 1
    )