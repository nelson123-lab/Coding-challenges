WITH D_ranking AS (
    SELECT 
        departmentId AS Department, 
        name AS Employee, 
        salary, 
        DENSE_RANK() OVER(PARTITION BY departmentId ORDER BY salary DESC) AS ranking 
    FROM Employee
)

SELECT 
    D.name AS Department, 
    E.Employee, 
    E.salary  
FROM D_ranking AS E 
LEFT JOIN Department AS D ON E.Department = D.id
WHERE E.ranking <= 3;

/*
- Here we need to rank the top 3 salaries of each department. Since the department can be N in numbers we cannot use UNION and combine the results from different
departments using LIMIT 3 and ORDER BY. 
- Another reason we cannot use LIMIT 3 is that the same salary can be repeated for different people, so unique 3 salaries can be 90k, 85k, 85k, and 70k.
- But it still can be achieved using limit but we have to GROUP BY salary first and then LIMIT the top 3 salaries and then keep this as a subquery to extract 
out all rows with the top 3 salaries

Here we are using DENSE_RANK() which ranks the partitions without gaps of ties. Here is an example below.

id | name  | salary
---|-------|-------
 1 | Alice | 5000
 2 | Bob   | 6000
 3 | Carol | 6000
 4 | Dave  | 7000
 5 | Eve   | 8000

-- With the below query.
```sql
SELECT
  id,
  name,
  salary,
  RANK() OVER (ORDER BY salary DESC) as rank,
  DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank
FROM
  employees;
```

**Result:**

| id | name  | salary | rank | dense_rank |
|----|-------|--------|------|------------|
|  5 | Eve   | 8000   | 1    | 1          |
|  4 | Dave  | 7000   | 2    | 2          |
|  2 | Bob   | 6000   | 3    | 3          |
|  3 | Carol | 6000   | 3    | 3          |
|  1 | Alice | 5000   | 5    | 4          |

- `RANK() OVER (ORDER BY salary DESC) as rank`: This calculates the rank with gaps for ties. ( School Ranking system )
- `DENSE_RANK() OVER (ORDER BY salary DESC) as dense_rank`: This calculates the rank without gaps for ties.

-- Now we will just extract the ranking <= 3 to get the top 3 salaries from each department (Partition).
*/
