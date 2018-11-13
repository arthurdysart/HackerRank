/*
HackerRank SQL: The Sum Function
https://www.hackerrank.com/challenges/revising-aggregations-sum
Difficulty: easy

Created on Mon Nov 12 10:17:51 2018
@author: Arthur Dysart
*/


SELECT
    SUM(population)
FROM
    city
WHERE
    district = 'California'
;