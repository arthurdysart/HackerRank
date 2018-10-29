/*
HackerRank SQL: Weather Observation Station 11
https://www.hackerrank.com/challenges/weather-observation-station-11
Difficulty: easy

Created on Sun Oct 28 17:02:41 2018
@author: Arthur Dysart
*/

SELECT DISTINCT CITY
FROM STATION
WHERE
    SUBSTRING(CITY, 1, 1) NOT IN ('a','e','i','o','u') OR
    SUBSTRING(CITY, -1, 1) NOT IN ('a','e','i','o','u');