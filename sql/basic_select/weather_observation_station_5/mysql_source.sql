/*
HackerRank SQL: Weather Observation Station 5
https://www.hackerrank.com/challenges/weather-observation-station-5
Difficulty: easy

Created on Sun Oct 28 16:49:21 2018
@author: Arthur Dysart
*/

-- Selects smallest city name and corresponding length (sorts by "city length" ascending, "city" ascending)
SELECT CITY, LENGTH(CITY) AS CITY_LENGTH
FROM STATION
ORDER BY CITY_LENGTH ASC, CITY ASC LIMIT 1;

-- Selects longest city name and corresponding length (sorts by "city length" descending, "city" ascending)
SELECT CITY, LENGTH(CITY) AS CITY_LENGTH
FROM STATION
ORDER BY CITY_LENGTH DESC, CITY ASC LIMIT 1;