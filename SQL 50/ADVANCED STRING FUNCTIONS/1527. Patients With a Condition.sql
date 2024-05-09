-- Write your MySQL query statement below
SELECT patient_id, patient_name, conditions FROM Patients WHERE conditions LIKE '% DIAB1%' OR conditions LIKE 'DIAB1%'

-- Here we are using a function called LIKE to check whether the word is present in the strings or not. The % symbol shows that there are other characters present on that side of the word.
