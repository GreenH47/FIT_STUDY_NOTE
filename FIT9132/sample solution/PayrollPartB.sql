/*
Databases PART B PAYROLL REVISION solution
PayrollPartB.sql

Databases Units
Author: FIT Database Teaching Team
License: Copyright Monash University, unless otherwise stated. All Rights Reserved.
COPYRIGHT WARNING
Warning
This material is protected by copyright. For use within Monash University only. NOT FOR RESALE.
Do not remove this notice.
*/

/*
1. Display for all employees their number, name, job, monthly salary, their 
current annual salary (not including commission) and what their annual salary 
would be if they were given a 10% pay rise. Order the output by employee number.
*/

SELECT
    empno,
    empname,
    empjob,
    empmsal,
    empmsal * 12          AS annual_salary,
    empmsal * 12 * 1.1    AS ann_sal_with_rise
FROM
    payroll.employee
ORDER BY
    empno;

/*
2. Display the name of all employees, their birthdate and their age in years. 
Order the output by birthdate, within birthdate order the output by name.
*/

SELECT
    empname,
    to_char(empbdate, 'DD-Mon-YYYY')                       AS birthdate,
    floor(months_between(sysdate, empbdate) / 12)          AS "Age in Yrs"
FROM
    payroll.employee
ORDER BY
    empbdate,
    empname;

-- Note must not order by birthdate column this is character data

/*
3. Display for all employees, their number, name, job, monthly salary, 
commission (which is paid monthly) and their current annual salary (including 
commission). Order the output by  employee number.
*/

SELECT
    empno,
    empname,
    empjob,
    empmsal,
    empcomm,
    ( empmsal + nvl(empcomm, 0) ) * 12 AS total_salary
FROM
    payroll.employee
ORDER BY
    empno;

--Q4. Display all employees details in the following format: EMPLOYEE N. Smith IS A Trainer AND WORKS IN THE Training DEPARTMENT.
SELECT
    'EMPLOYEE '
     || empinit
     || '. '
     || initcap(empname)
     || ' IS A '
     || initcap(empjob)
     || ' AND WORKS IN THE '
     || initcap(deptname)
     || ' DEPARTMENT.' as empdetails
FROM
    payroll.employee e
    JOIN payroll.department d ON (
        e.deptno = d.deptno
    )
ORDER BY empname;

SELECT
    'EMPLOYEE '
     || empinit
     || '. '
     || initcap(empname)
     || ' IS A '
     || initcap(nvl(empjob,'----'))
     || ' AND WORKS IN THE '
     || initcap(nvl(deptname,'----'))
     || ' DEPARTMENT.' as empdetails
FROM
    payroll.employee e
    left outer JOIN payroll.department d ON (
        e.deptno = d.deptno
    )
ORDER BY e.empno;

/*
5. Display the name of all employees, their birthdate and their age in months. 
Order the output by age in months (with the oldest employee first), within age 
in months order the output by name. The age in months must be shown with one 
decimal point and right aligned.
*/

SELECT
    empname,
    to_char(empbdate, 'dd-Mon-yyyy')                                     AS birthdate,
    lpad(to_char(months_between(sysdate, empbdate), '990.0'), 10)        AS age_in_months
FROM
    payroll.employee
ORDER BY
    age_in_months DESC,
    empname;

/*
6. Display the employees who were born in February. Order the output by employee
name.
*/

SELECT
    empname,
    to_char(empbdate, 'dd-Mon-yyyy') AS birthdate
FROM
    payroll.employee
WHERE
    EXTRACT(MONTH FROM empbdate) = 2
ORDER BY
    empname;

/*
7. Display the employee name, salary and commission (using the GREATEST function) 
for those employees who earn more commission than their monthly salary. Order 
the output by employee name and within name by monthly take home pay (salary 
plus commission).
*/

SELECT
    empname,
    empmsal,
    empcomm
FROM
    payroll.employee
WHERE
    empcomm = greatest(empcomm, empmsal)
ORDER BY
    empname,
    ( empmsal + empcomm );


/*
8. Display the name of all employees and their birthdate in the following 
format: EMPLOYEE N. Smith was born on FRIDAY the 17 of DECEMBER , 1982. 
Order the output by employee name.
*/

SELECT
    'EMPLOYEE '
     || empinit
     || '. '
     || initcap(empname)
     || ' was born on '
     || rtrim(TO_CHAR(empbdate,'DAY') )
     || ' the '
     || EXTRACT(DAY FROM empbdate)
     || ' of '
     || rtrim(TO_CHAR(empbdate,'MONTH') )
     || ','
     || EXTRACT(YEAR FROM empbdate) as "EMP DOB Details"
FROM
    payroll.employee
ORDER BY 
    empname;

/*
9. Display the name of the employees who have registered for a course and the
number of times they have registered. Order the output by employee number.
*/

SELECT
    e.empno,
    e.empname,
    COUNT(*) AS nbr_registrations
FROM
         payroll.employee e
    JOIN payroll.registration r
    ON ( e.empno = r.empno )
GROUP BY
    e.empno,
    e.empname
ORDER BY
    empno;

/*
10. Who is the oldest employee? Show the employee number, name and date of 
birth. Order the output by employee number.
*/

SELECT
    empno,
    empname,
    to_char(empbdate, 'DD-Mon-YYYY')
FROM
    payroll.employee
WHERE
    empbdate = (
        SELECT
            MIN(empbdate)
        FROM
            payroll.employee
    )
ORDER BY
    empno;

/*
11. For each department, list the department number and name, the number of 
employees, the minimum and maximum monthly salary, the total monthly salary and 
the average salary paid to their employees. 
Name the columns: NbrOfEmployees, MinSalary, MaxSalary, TotalSalary, AvgSalary. 
Order the output by department number.
*/

SELECT
    d.deptno,
    d.deptname,
    COUNT(e.empno)                           "NbrOfEmployees",
    MIN(empmsal)                             "MinSalary",
    MAX(empmsal)                             "MaxSalary",
    SUM(empmsal)                             "TotalSalary",
    to_char(AVG(empmsal), '9999.99')          "AvgSalary"
FROM
    payroll.employee      e
    RIGHT OUTER JOIN payroll.department    d
    ON ( e.deptno = d.deptno )
GROUP BY
    d.deptno,
    d.deptname
ORDER BY
    deptno;

/*
12. Display the department number, jobs available in that department and the 
total monthly salary paid for each job. Order the output by department number 
and within a department by job.
*/

SELECT
    deptno,
    empjob,
    SUM(empmsal)
FROM
    payroll.employee
GROUP BY
    deptno,
    empjob
ORDER BY deptno,empjob;

/*
13. Which employee earns more than the average salary? Show the employee number, 
name and monthly salary. Order the output by employee number.
*/

SELECT
    empno,
    empname,
    empmsal
FROM
    payroll.employee
WHERE
    empmsal > (
        SELECT
            AVG(empmsal)
        FROM
            payroll.employee
    )
ORDER BY 
    empno;

/*
14. Which department has the greatest average monthly salary? Show the 
department no, name and average monthly salary. Order the output by department 
number.
*/

SELECT
    d.deptno,
    d.deptname,
    round(AVG(empmsal),2) "AvgSalary"
FROM
    payroll.employee e
    JOIN payroll.department d ON (
        e.deptno = d.deptno
    )
GROUP BY
    d.deptno,
    d.deptname
HAVING
    AVG(empmsal) = (
        SELECT
            MAX(AVG(empmsal) )
        FROM
            payroll.employee
        GROUP BY
            deptno
    )
ORDER BY 
    deptno;

-- to_char could be used instead of round

/*
15. Which course has the most offerings? Show the course code, description and 
number of offerings. Order the output by the number of offerings in descending 
order and within the number of offerings by the course code.
*/

SELECT
    c.crscode,
    c.crsdesc,
    COUNT(*) "NbrOfferings"
FROM
         payroll.course c
    JOIN payroll.offering o
    ON ( c.crscode = o.crscode )
GROUP BY
    c.crscode,
    c.crsdesc
HAVING
    COUNT(*) = (
        SELECT
            MAX(COUNT(*))
        FROM
            payroll.offering
        GROUP BY
            crscode
    )
ORDER BY
    COUNT(*) DESC,
    crscode;

/*
16. Display the name, job and date of birth of employees who perform the same 
job as SCOTT and were born in the same year. Do not include SCOTT in the output. 
Order the output by employee name. 
*/

SELECT
    e.empname,
    e.empjob,
    to_char(empbdate, 'dd-Mon-yyyy')
FROM
    payroll.employee e
WHERE
        ( e.empjob,
          EXTRACT(YEAR FROM empbdate) ) = (
            SELECT
                e.empjob,
                EXTRACT(YEAR FROM empbdate)
            FROM
                payroll.employee e
            WHERE
                upper(empname) = 'SCOTT'
        )
    AND upper(e.empname) <> 'SCOTT'
ORDER BY
    empname;

/*
17. Using the MINUS statement, which employees have never registered in a course. 
Show their employee number and name. Order the output by employee number.
*/

SELECT
    empno,
    empname
FROM
    payroll.employee
MINUS
SELECT DISTINCT
    e.empno,
    empname
FROM
         payroll.registration r
    JOIN payroll.employee e
    ON ( r.empno = e.empno )
ORDER BY
    empno;

/*
18. Using the INTERSECT statement, which employees have both registered for and 
conducted courses. Show the employee number and name. Order the output by 
employee number.
*/

SELECT DISTINCT
    e.empno AS "TrainerAndStudent",
    empname
FROM
         payroll.offering o
    JOIN payroll.employee e
    ON ( o.empno = e.empno )
INTERSECT
SELECT DISTINCT
    e.empno,
    empname
FROM
         payroll.registration r
    JOIN payroll.employee e
    ON ( r.empno = e.empno )
ORDER BY
    "TrainerAndStudent";


