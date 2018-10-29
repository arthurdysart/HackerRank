/*
HackerRank SQL: Employee Salaries
https://www.hackerrank.com/challenges/salary-of-employees
Difficulty: easy

Created on Sun Oct 28 17:20:01 2018
@author: Arthur Dysart
*/

SELECT name
FROM Employee
WHERE
    salary>2000 AND
    months<10;