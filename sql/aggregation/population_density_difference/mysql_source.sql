/*
HackerRank SQL: Population Density Difference
https://www.hackerrank.com/challenges/population-density-difference
Difficulty: easy

Created on Mon Nov 12 11:23:57 2018
@author: Arthur Dysart
*/


SELECT
    MAX(population) - MIN(population)
        AS population_density_difference
FROM
    city;