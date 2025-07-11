-- # Write your MySQL query statement below
-- SELECT 
--   ROUND(
--     COUNT(DISTINCT a.player_id) * 1.0 / 
--     (SELECT COUNT(DISTINCT player_id) FROM Activity), 
--     2
--   ) AS fraction
-- FROM Activity a
-- WHERE (a.player_id, a.event_date) IN (
--   SELECT player_id, DATE_ADD(MIN(event_date), INTERVAL 1 DAY)
--   FROM Activity
--   GROUP BY player_id
-- );
# Write your MySQL query statement below
SELECT ROUND(COUNT(DISTINCT player_id) / (SELECT COUNT(DISTINCT player_id) FROM Activity), 2) as fraction
FROM Activity
WHERE (player_id, DATE_SUB(event_date, INTERVAL 1 DAY))
IN (SELECT player_id, MIN(event_date) AS first_login FROM ACTIVITY GROUP BY player_id)
