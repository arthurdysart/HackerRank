/*
HackerRank SQL: Weather Observation Station 18
https://www.hackerrank.com/challenges/weather-observation-station-18
Difficulty: easy

Created on Mon Nov 12 10:19:07 2018
@author: Arthur Dysart
*/


/*
Solution
ROUND( MAX(), MIN())
*/
SELECT
    ROUND(MAX(long_w) - MIN(long_w) + MAX(lat_n) - MIN(lat_n), 4)
FROM
    station
;