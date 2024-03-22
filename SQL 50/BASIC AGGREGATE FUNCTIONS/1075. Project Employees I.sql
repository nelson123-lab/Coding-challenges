-- Solution using JOINS
SELECT P.project_id , ROUND(AVG(E.experience_years), 2) as average_years FROM Project as P LEFT JOIN Employee as E ON P.employee_id = E.employee_id
GROUP BY P.project_id

-- Solution using Subqueries
select P.project_id, round(avg(E.experience_years),2) as average_years
from Project P, Employee E
where P.employee_id  =E.employee_id
group by  P.project_id
