/*
HackerRank SQL: Average Population
https://www.hackerrank.com/challenges/average-population
Difficulty: easy

Created on Mon Nov 12 10:23:41 2018
@author: Arthur Dysart
*/


SELECT
    ROUND(AVG(population), 0)
        AS average_population 
FROM
    city;