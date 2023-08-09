/* Write your MySQL query statement below */
select EU.unique_id, E.name from Employees as E left join EmployeeUNI as EU ON EU.id = E.id

/* Here the EmployeeUNI table is represented as EU and Employees table as E.
We are using left join because we need all the user information irrespective of whether of them present in the EU table. The left join works in the same way. 
It will return all the employees of left table irrespective of whether they have a matching id in EU table or not. */

