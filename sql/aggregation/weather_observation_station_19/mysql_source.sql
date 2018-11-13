/*
HackerRank SQL: Weather Observation Station 19
https://www.hackerrank.com/challenges/weather-observation-station-19
Difficulty: easy

Created on Mon Nov 12 15:12:05 2018
@author: Arthur Dysart
*/


/*
Solution
ROUND( POWER(), MAX(), MIN())
*/
SELECT
    -- Apply Pythagorean theorem to determine Euclidean distance
    ROUND(SQRT(POWER(MAX(long_w) - MIN(long_w), 2) + POWER(MAX(lat_n) - MIN(lat_n),2)), 4)
FROM
    station
;