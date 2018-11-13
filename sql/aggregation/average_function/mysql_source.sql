/*
HackerRank SQL: The Average Function
https://www.hackerrank.com/challenges/revising-aggregations-the-average-function
Difficulty: easy

Created on Mon Nov 12 10:19:45 2018
@author: Arthur Dysart
*/


SELECT
    AVG(population)
FROM
    city
WHERE
    district = 'California'
;