/*
HackerRank SQL: Weather Observation Station 9
https://www.hackerrank.com/challenges/weather-observation-station-9
Difficulty: easy

Created on Sun Oct 28 17:00:25 2018
@author: Arthur Dysart
*/

SELECT DISTINCT CITY
FROM STATION
WHERE SUBSTRING(CITY, 1, 1) NOT IN ('a','e','i','o','u');