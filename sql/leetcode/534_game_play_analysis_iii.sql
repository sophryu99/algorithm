-- https://leetcode.com/problems/game-play-analysis-iii/

-- # Write your MySQL query statement below

-- # 1. Self join on event_date where t1.event date is later than t2.event date
-- # 2. Group by the Sum t2.games_played which is the total number of games played until t1.even date

-- # ["player_id", "event_date", "event_date"], 
-- # [[1, "2017-06-25", "2016-03-01"], 
-- #  [1, "2016-05-02", "2016-03-01"], 
-- #  [1, "2016-03-01", "2016-03-01"], 
-- #  [1, "2017-06-25", "2016-05-02"], 
-- #  [1, "2016-05-02", "2016-05-02"], 
-- #  [1, "2017-06-25", "2017-06-25"], 
-- #  [3, "2018-07-03", "2016-03-02"], 
-- #  [3, "2016-03-02", "2016-03-02"], 
-- #  [3, "2018-07-03", "2018-07-03"]]}

select a1.player_id, a1.event_date, SUM(a2.games_played) as games_played_so_far
from activity as a1
inner join activity as a2
on a1.event_date >= a2.event_date
and a1.player_id = a2.player_id
group by  a1.player_id, a1.event_date