/*
Databases PART A PAYROLL REVISION solution
PayrollPartA.sql

Databases Units
Author: FIT Database Teaching Team
License: Copyright Monash University, unless otherwise stated. All Rights Reserved.
COPYRIGHT WARNING
Warning
This material is protected by copyright. For use within Monash University only. NOT FOR RESALE.
Do not remove this notice.
*/

/*
1. Display the full details of employees who earn less than $1000, order the 
output  by  the employee number.
*/

SELECT
    empno,
    empname,
    empinit,
    empjob,
    to_char(empbdate,'dd Mon yyyy'),
    empmsal,
    empcomm,
    deptno,
    mgrno
FROM
    payroll.employee
WHERE
    empmsal < 1000
ORDER BY
    empno;

/*
2. List the department number of departments that have employees, order 
the output by the department number .
*/

SELECT DISTINCT
    deptno
FROM
    payroll.employee
ORDER BY deptno;

/*
3. Display the full details of trainers (employee job is TRAINER) who earn less 
than 2500 each month and are working in department 20. Order the output by  
employee number.
*/

SELECT
    empno,
    empname,
    empinit,
    empjob,
    to_char(empbdate,'dd Mon yyyy'),
    empmsal,
    empcomm,
    deptno,
    mgrno
FROM
    payroll.employee
WHERE
    upper(empjob) = 'TRAINER'
    AND empmsal < 2500
    AND deptno = 20
ORDER BY
    empno;
    
/*
4. Display the name, job, monthly salary and commission of employees whose 
monthly salary is higher than their commission. Rename the columns: Name, Job, 
Monthly Salary and Commission. Order the output by name and within name by 
descending monthly salary.
*/

SELECT
    empname  AS "Name",
    empjob   AS "Job",
    empmsal  AS "Monthly Salary",
    empcomm  AS "Commission"
FROM
    payroll.employee
WHERE
    empmsal > empcomm
ORDER BY
    empname,
    empmsal DESC;

/*
5. Display the name and job of employees whose job ends with the letter R. 
Order the output by name and within name by job.
*/

SELECT
    empname,
    empjob
FROM
    payroll.employee
WHERE
    upper(empjob) LIKE '%R'
ORDER BY
    empname,
    empjob;

/*
6. Display the name and job of employees that have a name starting with “J”, 
“K” or “M”. Order the output by name and within name by job.
*/

SELECT
    empname,
    empjob
FROM
    payroll.employee
WHERE
        upper(empname) LIKE 'J%'
    OR
        upper(empname) LIKE 'K%'
    OR
        upper(empname) LIKE 'M%'
ORDER BY
    empname,
    empjob;

/*
7. Display the name, job, date of birth and monthly salary of employees who 
were born before 1990 and earn more than 1500 each month. Order the output by 
name and within name by monthly salary.
*/


SELECT
    empname,
    empjob,
    to_char(empbdate, 'Dd-Mon-YYYY') AS birthdate,
    empmsal
FROM
    payroll.employee
WHERE
        empbdate < TO_DATE('01-JAN-1990', 'dd-MON-YYYY')
    AND empmsal > 1500
ORDER BY
    empname,
    empmsal;

/*
8. Display the name, job, date of birth and salary of employees that don't have 
a commission. Order the output by name, and within name by date of birth.
*/

SELECT
    empname,
    empjob,
    to_char(empbdate, 'Dd-Mon-YYYY') AS birthdate,
    empmsal
FROM
    payroll.employee
WHERE
    empcomm IS NULL
ORDER BY
    empname,
    empbdate;

/*
9. Display the employee name, job, department name, location and monthly salary
of employees that work in NEW YORK. Order the output by name, and within name 
by job.
*/

SELECT
    e.empname,
    e.empjob,
    d.deptname,
    d.deptlocation,
    e.empmsal
FROM
    payroll.employee e join payroll.department d on e.deptno = d.deptno
WHERE
    upper(d.deptlocation) = 'NEW YORK'
ORDER BY e.empname;

/*
10. Display the name and job of employees who do not work in NEW YORK or CHICAGO. 
Order the output by name, and within name by job.
*/

SELECT
    e.empname,
    e.empjob,
    d.deptname,
    d.deptlocation
FROM
         payroll.employee e
    JOIN payroll.department d
    ON e.deptno = d.deptno
WHERE
    upper(d.deptlocation) NOT IN ( 'NEW YORK', 'CHICAGO' )
ORDER BY
    e.empname,
    empjob;

/*
11. Display the name, job, date of birth and salary of employees who were born
in the first half of the 70s. Display the output in birth date order and 
within birthdate by name.
*/

SELECT
    empname,
    empjob,
    to_char(empbdate, 'Dd-Mon-YYYY') AS birthdate,
    empmsal
FROM
    payroll.employee
WHERE
    empbdate BETWEEN TO_DATE('01-JAN-1970', 'DD-MON-YYYY') AND TO_DATE('31-DEC-1974',
    'DD-MON-YYYY')
ORDER BY
    empbdate,
    empname;
    
/* 
12.  Display the name, job and salary of employees who earn less than 1500 
or greater than 3000 per month. Order the output by name, and within name by 
monthly salary.
*/

SELECT
    empname,
    empjob,
    empmsal
FROM
    payroll.employee
WHERE
    empmsal NOT BETWEEN 1500 AND 3000
ORDER BY
    empname,
    empmsal;
    

/* 
13. Display the name, job and manager number of employees who have a manager. 
Order the output by manager number and within a given manager by employee name.
*/

SELECT
    empname,
    empjob,
    mgrno
FROM
    payroll.employee
WHERE
    mgrno IS NOT NULL
ORDER BY
    mgrno,
    empname;

/*
14. Display the name, job, department name, department location and monthly 
salary of employees who either work in DALLAS or as a MANAGER, and earn more 
than 2500. Order the output by name and within name by monthly salary.
*/

SELECT
    e.empname,
    e.empjob,
    d.deptname,
    d.deptlocation,
    e.empmsal
FROM
         payroll.employee e
    JOIN payroll.department d
    ON ( e.deptno = d.deptno )
WHERE
    ( upper(d.deptlocation) = 'DALLAS'
      OR upper(e.empjob) = 'MANAGER' )
    AND e.empmsal > 2500
ORDER BY
    e.empname,
    empmsal;

/*
15. Display the name, job, monthly salary and salary grade of all employees. 
Display the list in monthly salary order within salary grade order.
*/

SELECT
    e.empname,
    e.empjob,
    e.empmsal,
    s.salgrade
FROM
    payroll.employee e
    JOIN payroll.salgrade s ON (
        e.empmsal BETWEEN s.sallower AND s.salupper
    )
ORDER BY
    s.salgrade,
    e.empmsal;

/*
16. Display the name and location of ALL departments, and the name of their 
employees. Display the output in employee name order within department name order.
*/

SELECT
    d.deptname,
    d.deptlocation,
    e.empname
FROM
    payroll.employee e
    RIGHT OUTER JOIN payroll.department d ON (
        e.deptno = d.deptno
    )
ORDER BY
    d.deptname,
    e.empname;

/*
17. Display the name of ALL employees, their job and the name of their manager. 
List the output in employee name order within manager name order.
*/

SELECT
    e.empname "Employee",
    e.empjob AS "Emp Job",
    m.empname AS "Manager"
FROM
    payroll.employee e
    LEFT OUTER JOIN payroll.employee m ON (
        e.mgrno = m.empno
    )
ORDER BY
    m.empname,
    e.empname;
    
-- here NVL(m.empname,'NA') could be used to display a value rather than leave the 
-- managers name null for the director

/*
18. For each employee display their employment history. In the listing include 
the employees’ name, the name of the department they worked for, the begin and 
end date and their monthly salary. Display the output in begin date order 
(most recent at the top of the list) within employee name order.
*/

SELECT
    e.empname,
    d.deptname,
    to_char(histbegindate,'DD-Mon-YYY') as HISTBEGIN,
    to_char(histenddate,'Dd-Mon-YYYY') as HISTEND,
    h.histmsal
FROM
    payroll.employee e
    JOIN payroll.history h ON (
        e.empno = h.empno
    )
    JOIN payroll.department d ON (
        d.deptno = h.deptno
    )
ORDER BY
    e.empname,
    h.histbegindate DESC;

/*
19. Display the employee name, empjob, monthly salary and annual salary of all 
employees (annual salary is monthly salary x 12). Order the output by annual 
salary with the highest value shown first and within annual salary by name.
*/

SELECT
    empname,
    empjob,
    empmsal,
    empmsal * 12 AS "Annual Salary"
FROM
    payroll.employee
ORDER BY
    "Annual Salary" DESC,
    empname;

/*
20. Display the employee name, empjob, monthly salary, empcommission and 
annual income (salary and empcommission) of all employees. Commission is paid 
on a monthly basis. Order the output by name,and within by annual income.
*/

SELECT
    empname,
    empjob,
    empmsal,
    empcomm,
    12 * ( empmsal + nvl(empcomm, 0) ) AS "Annual Income"
FROM
    payroll.employee
ORDER BY
    empname,
    "Annual Income";
