# helps to combine rows together unlike join which helps to join columns together

# UNION

SELECT first_name,last_namae FROM employee_demographics UNION SELECT first_name,last_name FROM employee_salaries 

union removes duplicate values 

usecase - we need firstname and last name where age > 50  and  whose salary > 70k 

SELECT first_name,last_name,'OLD' AS Label
FROM employee_demographics
WHERE age > 50 
UNION 
SELECT first_name,Last_name,'Highly Paid Employee' AS Label
FROM employee_salary 
WHERE salary > 70000
; 