/*
HackerRank SQL: Weather Observation Station 15
https://www.hackerrank.com/challenges/weather-observation-station-15
Difficulty: easy

Created on Mon Nov 12 13:39:06 2018
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
    lat_n < 137.2345
ORDER BY
    lat_n DESC
LIMIT
    1
;


/*
Solution 2
ROUND() / WHERE clause / SQ: [max() / WHERE clause] 
*/
SELECT
    ROUND(long_w, 4)
FROM
    station
WHERE
    lat_n = (SELECT
                MAX(lat_n)
             FROM
                station
             WHERE
              lat_n < 137.2345)
;