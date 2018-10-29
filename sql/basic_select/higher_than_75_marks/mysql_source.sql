/*
HackerRank SQL: Higher Than 75 Marks
https://www.hackerrank.com/challenges/more-than-75-marks
Difficulty: easy

Created on Sun Oct 28 17:14:15 2018
@author: Arthur Dysart
*/

SELECT Name
FROM STUDENTS
WHERE Marks>75
ORDER BY SUBSTRING(Name,-3,3) ASC, ID ASC;