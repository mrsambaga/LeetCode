/* Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 
Write an SQL query to report all the duplicate emails.
Return the result table in any order.
The query result format is in the following example. */

/* Solution 1 */
SELECT DISTINCT email
FROM (
    SELECT id, email, COUNT(email) AS number
    FROM Person
    GROUP BY email
) duplicate
WHERE number > 1

/* Solution 2 */
SELECT email
FROM Person
GROUP BY email
HAVING COUNT(email) > 1

/* For the first solution, i use subquery to count the duplicate and then filter using WHERE. Turns out, i can just filter without subquery by using 
HAVING and GROUP BY to count the number of email for every email */
