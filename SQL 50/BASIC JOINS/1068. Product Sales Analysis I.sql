# Write your MySQL query statement below
select p.product_name, s.year, s.price from Sales as s left join Product as p on p.product_id = s.product_id;

/* Here left join is used to ensure all the rows from Sales tables are included even if there is no matching product id in Products table 
This is a explicit way of using join.*/


select product.product_name,sales.year,sales.price 
from sales,product 
where sales.product_id=product.product_id;

/* This is a solution without using join. It is an implicit way of using join. HEre, the where condition joins the table.
