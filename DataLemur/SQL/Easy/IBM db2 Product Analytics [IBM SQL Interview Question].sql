WITH employee_queries AS (
    SELECT E.employee_id,
           COALESCE(COUNT(DISTINCT Q.query_id), 0) AS unique_queries
    FROM employees AS E
    LEFT JOIN queries AS Q ON Q.employee_id = E.employee_id
                           AND EXTRACT(MONTH FROM Q.query_starttime) BETWEEN 7 AND 9
    GROUP BY E.employee_id
)

SELECT unique_queries,
       COUNT(employee_id) AS employee_count
FROM employee_queries
GROUP BY unique_queries
ORDER BY unique_queries;

"""
- Here the employee table contains all the information about the employee with their employee_id and name.
- We need to check the usage of queries by different employees for that we need to keep all the information of employees and get the queries of all 
  employees who did queries.
- We use a LEFT JOIN with employees tables as the LEFT and the Queries table as the RIGHT.
- We need to only check for the dates between July to september which is why we used EXTRACT(MONTH FROM Q.query_starttime) BETWEEN 7 AND 9
"""