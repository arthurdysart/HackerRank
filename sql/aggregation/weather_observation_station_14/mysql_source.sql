/*
HackerRank SQL: Weather Observation Station 14
https://www.hackerrank.com/challenges/weather-observation-station-14
Difficulty: easy

Created on Mon Nov 12 13:32:56 2018
@author: Arthur Dysart
*/


/*
Solution 1
TRUNCATE(MAX()) / WHERE clause
*/
SELECT
    TRUNCATE(MAX(lat_n), 4)
FROM
    station
WHERE
    lat_n < 137.2345
;


/*
Solution 3
TRUNCATE() / WHERE clause / ORDER BY / LIMIT
*/
SELECT
    TRUNCATE(lat_n, 4)
FROM
    station
WHERE
    lat_n < 137.2345
ORDER BY
    lat_n DESC
LIMIT
    1
;