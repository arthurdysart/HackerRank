/*
HackerRank SQL: Weather Observation Station 12
https://www.hackerrank.com/challenges/weather-observation-station-12
Difficulty: easy

Created on Sun Oct 28 17:04:43 2018
@author: Arthur Dysart
*/

SELECT DISTINCT CITY
FROM STATION
WHERE
    SUBSTRING(CITY, 1, 1) NOT IN ('a','e','i','o','u') AND
    SUBSTRING(CITY, -1, 1) NOT IN ('a','e','i','o','u');