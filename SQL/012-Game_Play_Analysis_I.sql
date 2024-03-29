/* Table: Activity

+--------------+---------+
| Column Name  | Type    |
+--------------+---------+
| player_id    | int     |
| device_id    | int     |
| event_date   | date    |
| games_played | int     |
+--------------+---------+
(player_id, event_date) is the primary key of this table.
This table shows the activity of players of some games.
Each row is a record of a player who logged in and played a number of games (possibly 0) before logging out on someday using some device.
 
Write an SQL query to report the first login date for each player.
Return the result table in any order.
The query result format is in the following example. */

SELECT DISTINCT player_id, min(event_date) AS first_login
FROM Activity
GROUP BY player_id

/* For this problem, if we want to get the min date for every id, we can just group by id first then use min(event_date) to find minimum date for every different id */

