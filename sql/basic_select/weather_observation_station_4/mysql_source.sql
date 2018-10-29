/*
HackerRank SQL: Weather Observation Station 4
https://www.hackerrank.com/challenges/weather-observation-station-4
Difficulty: easy

Created on Sun Oct 28 16:29:56 2018
@author: Arthur Dysart
*/

SELECT COUNT(CITY) - COUNT(DISTINCT CITY)
FROM STATION;