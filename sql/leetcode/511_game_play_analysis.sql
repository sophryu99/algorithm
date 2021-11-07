-- https://leetcode.com/problems/game-play-analysis-i/

-- # Logic:
-- # 1. Group by the activity table by the smallest datetime

SELECT player_id, MIN(event_date) as first_login
FROM Activity
GROUP BY player_id
