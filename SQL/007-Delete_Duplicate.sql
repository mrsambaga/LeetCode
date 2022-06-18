/*Table: Person

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| email       | varchar |
+-------------+---------+
id is the primary key column for this table.
Each row of this table contains an email. The emails will not contain uppercase letters.
 

Write an SQL query to delete all the duplicate emails, keeping only one unique email with the smallest id. Note that you are supposed to write a DELETE statement and not a SELECT one.

After running your script, the answer shown is the Person table. The driver will first compile and run your piece of code and then show the Person table. The final order of the Person table does not matter.

The query result format is in the following example.*/

/* Optimal solution (by : fabrizio3) : */
DELETE p1
FROM Person p1, Person p2
WHERE p1.email = p2.email AND p1.id > p2.id

/* For this problem we can join the table with itself temporary. By doing this, the second table will have the same id for the same person. We can take advantage of this
to check wheter if the person from the first table has the same email but bigger id than the person on the 2nd table. If yes, then we can delete it.*/
