/*
HackerRank SQL: Weather Observation Station 2
https://www.hackerrank.com/challenges/weather-observation-station-2
Difficulty: easy

Created on Mon Nov 12 12:28:48 2018
@author: Arthur Dysart
*/

SELECT
    ROUND(SUM(lat_n), 2)
        AS sum_lat,
    ROUND(SUM(long_w), 2)
        AS sum_long
FROM
    station
;