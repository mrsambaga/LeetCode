/* Table: Weather

+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| recordDate    | date    |
| temperature   | int     |
+---------------+---------+
id is the primary key for this table.
This table contains information about the temperature on a certain day.
 
Write an SQL query to find all dates' Id with higher temperatures compared to its previous dates (yesterday).
Return the result table in any order.
The query result format is in the following example. */

SELECT wt1.id 
FROM Weather wt1, Weather wt2
WHERE wt1.temperature > wt2.temperature AND TO_DAYS(wt1.recordDate)-TO_DAYS(wt2.recordDate)=1

/* We can use TO_DAYS() to get the number of days between year 0 to date for date type data. Then we can find the subtraction between 2 date equal 1 meaning the
date from first table is 1 day after the day from the 2nd table */
