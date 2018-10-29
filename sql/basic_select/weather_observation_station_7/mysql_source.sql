/*
HackerRank SQL: Weather Observation Station 7
https://www.hackerrank.com/challenges/weather-observation-station-7
Difficulty: easy

Created on Sun Oct 28 16:55:02 2018
@author: Arthur Dysart
*/

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY, -1, 1) IN ('a','e','i','o','u');