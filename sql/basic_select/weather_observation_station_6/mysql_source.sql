/*
HackerRank SQL: Weather Observation Station 6
https://www.hackerrank.com/challenges/weather-observation-station-6
Difficulty: easy

Created on Sun Oct 28 16:52:43 2018
@author: Arthur Dysart
*/

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY, 1, 1) IN ('a','e','i','o','u');