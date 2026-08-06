# Joins

two table employee_demo , employee_salary

## inner join 
    Select * From employee_demo INNER JOIN employee_salary ON employee_demo.employee_id = employee_salary.employee_id;

    or 
    SELECT * FROM employee_demo AS dem INNER JOIN employee_salary AS sal ON dem.employee_id = sal.employee_id;

## outer Joins
### Left JOins 
    SELECT dem.employee_id,age,occupation
    FROM employee_demographics AS dem
    LEFT JOIN employee_salary AS sal
    ON dem.employee_id = sal.employee_id;

    we take everything from left table and produces the match of it with right table 
### Right Join
    SELECT dem.employee_id,age,occupation
    FROM employee_demographics AS dem
    RIGHTa JOIN employee_salary AS sal
    ON dem.employee_id = sal.employee_id;

### SELF JOIN

    SELECT * FROM employee_salary emp1
    JOIN employee_salary emp2
    ON emp1.employee_id = emp2.employee_id

    # but lets say we want to assign a employye 1 with employee 2 and so we can use self join


    SELECT * FROM employee_salary emp1
    JOIN employee_salary emp2
    ON emp1.employee_id + 1 = emp2.employee_id

### joining multiple tables together

    SELECT * FROM enployee_dem AS dem INNER JOIN employee_salary AS sal ON dem.employee_id = sal.employee_id
    INNER JOIN  parks_department AS pd ON sal.dept_id = pd.department_id;