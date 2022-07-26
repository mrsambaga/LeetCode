/* Table: Employee

+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| id          | int     |
| name        | varchar |
| salary      | int     |
| managerId   | int     |
+-------------+---------+
id is the primary key column for this table.
Each row of this table indicates the ID of an employee, their name, salary, and the ID of their manager.

Write an SQL query to find the employees who earn more than their managers.
Return the result table in any order.
The query result format is in the following example. */

SELECT A.name AS Employee
FROM Employee A
INNER JOIN (
    SELECT *
    FROM Employee
) manager ON A.managerId = manager.id
WHERE A.salary > manager.salary

/* For this problem we can use inner join to join table 1 with employee only and table 2 with manager only. 
Then we can filter the employe salary to be greater than manager salary */
