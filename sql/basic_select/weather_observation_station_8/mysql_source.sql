/*
HackerRank SQL: Weather Observation Station 8
https://www.hackerrank.com/challenges/weather-observation-station-8
Difficulty: easy

Created on Sun Oct 28 16:57:17 2018
@author: Arthur Dysart
*/

SELECT DISTINCT CITY
FROM STATION
WHERE
    SUBSTRING(CITY, 1, 1) IN ('a','e','i','o','u') AND
    SUBSTRING(CITY, -1, 1) IN ('a','e','i','o','u');