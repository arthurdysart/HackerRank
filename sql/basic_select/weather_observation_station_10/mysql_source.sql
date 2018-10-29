/*
HackerRank SQL: Weather Observation Station 10
https://www.hackerrank.com/challenges/weather-observation-station-10
Difficulty: easy

Created on Sun Oct 28 17:01:36 2018
@author: Arthur Dysart
*/

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY, -1, 1) NOT IN ('a','e','i','o','u');