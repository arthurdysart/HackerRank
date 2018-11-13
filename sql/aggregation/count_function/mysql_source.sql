/*
HackerRank SQL: The Count Function
https://www.hackerrank.com/challenges/revising-aggregations-the-count-function
Difficulty: easy

Created on Mon Nov 12 10:15:32 2018
@author: Arthur Dysart
*/


SELECT
    COUNT(id)
FROM
    city
WHERE
    population > 100000
;