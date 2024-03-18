-- Write your MySQL query statement below
select s.student_id , s.student_name, sub.subject_name,COALESCE(count(e.student_id),0) as attended_exams  from students s Cross Join Subjects sub
left join Examinations e on e.student_id = s.student_id and  sub.subject_name =  e.subject_name
group by s.student_id , s.student_name, sub.subject_name order by s.student_id, sub.subject_name

"""
- Here we are using Cross join to get all the combinations of the names along with the subjects. For example 4 people with 3 subjects that is 12 combinations.
- COALESCE is used to handle the null case whenever there is null value keep it as 0.
"""
