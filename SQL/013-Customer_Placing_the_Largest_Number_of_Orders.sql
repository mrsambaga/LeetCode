/* Table: Orders

+-----------------+----------+
| Column Name     | Type     |
+-----------------+----------+
| order_number    | int      |
| customer_number | int      |
+-----------------+----------+
order_number is the primary key for this table.
This table contains information about the order ID and the customer ID.
 
Write an SQL query to find the customer_number for the customer who has placed the largest number of orders.
The test cases are generated so that exactly one customer will have placed more orders than any other customer.
The query result format is in the following example. */

SELECT customer_number
FROM Orders
GROUP BY customer_number
ORDER BY count(order_number) DESC
LIMIT 1

/* This problem want us to count the total order from every customer and the pick the largest one. We can do this by using group by customer and then count
order number to count the number of order for every customer. Then we can order by descending and limit 1 to get the largest order. */
