WITH dup_com_cte AS (
    SELECT 
        company_id 
    FROM 
        job_listings
    GROUP BY 
        company_id, 
        title, 
        description 
    HAVING 
        COUNT(company_id) > 1
)

SELECT 
    COUNT(company_id) AS duplicate_companies 
FROM 
    dup_com_cte;

-- Explanation
/*
- Here we are grouping by company_id, title, and description to find the company_id with the same job listings posted with the same job description.
- Then counting the number of the company_id to find the no of duplicate companies.
*/


