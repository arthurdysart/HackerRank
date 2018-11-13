/*
HackerRank SQL: The Blunder
https://www.hackerrank.com/challenges/the-blunder
Difficulty: easy

Created on Mon Nov 12 11:39:14 2018
@author: Arthur Dysart
*/


SELECT
    -- CEILING() returns smallest integer greater than or equal to argument
    -- REPLACE() maps specified character(s) in argument attribute
    CEILING(AVG(salary) - AVG(REPLACE(salary, '0', '')))
        AS salary_error 
FROM
    employees;