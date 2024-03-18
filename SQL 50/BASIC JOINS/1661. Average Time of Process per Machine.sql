-- Write your MySQL query statement below
SELECT A.machine_id, ROUND(AVG(A.timestamp - B.timestamp), 3) as processing_time FROM Activity as A JOIN Activity as B
ON A.machine_id = B.machine_id AND A.process_id = B.process_id AND A.activity_type = 'end' AND B.activity_type = 'start'
GROUP BY A.machine_id 

"""
- Here the same table is taken in different names and joined togehter on machine_id, process_id and along with conditions activity_type = "end" and activity_type = "start"
- The above step creats two colums containing the timestamps of end and timestamps of start. 
- We can obtain the process time by finding the difference between them.
"""
