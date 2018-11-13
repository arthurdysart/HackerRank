/*
HackerRank SQL: Weather Observation Station 16
https://www.hackerrank.com/challenges/weather-observation-station-16
Difficulty: easy

Created on Mon Nov 12 13:59:38 2018
@author: Arthur Dysart
*/


/*
Solution
ROUND() / WHERE clause / ORDER BY / LIMIT
*/
SELECT
    ROUND(long_w, 4)
FROM
    station
WHERE
    lat_n > 38.7780
ORDER BY
    lat_n ASC
LIMIT
    1
;


/*
Solution 2
ROUND() / WHERE clause / SQ[MIN() / WHERE clause]
*/
SELECT
    ROUND(long_w, 4)
FROM
    station
WHERE
    lat_n = (SELECT
                MIN(lat_n)
             FROM
                station
             WHERE
                lat_n > 38.7780)
;