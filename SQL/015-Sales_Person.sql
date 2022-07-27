/* Table: SalesPerson
+-----------------+---------+
| Column Name     | Type    |
+-----------------+---------+
| sales_id        | int     |
| name            | varchar |
| salary          | int     |
| commission_rate | int     |
| hire_date       | date    |
+-----------------+---------+
sales_id is the primary key column for this table.
Each row of this table indicates the name and the ID of a salesperson alongside their salary, commission rate, and hire date.
 

Table: Company
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| com_id      | int     |
| name        | varchar |
| city        | varchar |
+-------------+---------+
com_id is the primary key column for this table.
Each row of this table indicates the name and the ID of a company and the city in which the company is located.
 

Table: Orders
+-------------+------+
| Column Name | Type |
+-------------+------+
| order_id    | int  |
| order_date  | date |
| com_id      | int  |
| sales_id    | int  |
| amount      | int  |
+-------------+------+
order_id is the primary key column for this table.
com_id is a foreign key to com_id from the Company table.
sales_id is a foreign key to sales_id from the SalesPerson table.
Each row of this table contains information about one order. This includes the ID of the company, the ID of the salesperson, the date of the order, and the amount paid.

Write an SQL query to report the names of all the salespersons who did not have any orders related to the company with the name "RED".
Return the result table in any order.
The query result format is in the following example. */

SELECT P.name
FROM SalesPerson P
LEFT JOIN Orders O ON O.sales_id = P.sales_id
LEFT JOIN Company C ON O.com_id = C.com_id
GROUP BY P.name
HAVING COUNT(order_id)=0 OR SUM(C.name='RED')=0

/* For this problem, we have to use left join to join the table and we cannot use inner join. This is because there are sales person who doesnt have any order, so
if we use inner join, it will be deleted. After we use left join, we can use group by name and then filter by count the order id and check if it 0 and the sum the
company name RED. This is to check if the sales person has orders but not on RED company or the sales person doesnt have any order. */

