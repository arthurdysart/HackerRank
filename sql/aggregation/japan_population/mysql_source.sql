/*
HackerRank SQL: Japan Population
https://www.hackerrank.com/challenges/japan-population
Difficulty: easy

Created on Mon Nov 12 10:33:33 2018
@author: Arthur Dysart
*/


SELECT
    SUM(population) 
FROM
    city 
WHERE
    countrycode = 'JPN'
; 