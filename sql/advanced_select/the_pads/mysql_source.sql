/*
HackerRank SQL: The PADS
https://www.hackerrank.com/challenges/the-pads
Difficulty: medium

Created on Sun Oct 28 18:02:01 2018
@author: Arthur Dysart
*/

-- Formats output string containing all names and occupation identifier
SELECT CONCAT(Name,'(',SUBSTRING(Occupation, 1, 1),')')
FROM OCCUPATIONS
ORDER BY Name ASC;

-- Formats output string containing counts of occupations
SELECT CONCAT('There are a total of ', COUNT(Occupation), ' ', LOWER(Occupation), 's.')
FROM OCCUPATIONS
GROUP BY Occupation
ORDER BY COUNT(Occupation) ASC, Occupation ASC;