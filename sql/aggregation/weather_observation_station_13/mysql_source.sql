/*
HackerRank SQL: Weather Observation Station 13
https://www.hackerrank.com/challenges/weather-observation-station-13
Difficulty: easy

Created on Mon Nov 12 13:29:46 2018
@author: Arthur Dysart
*/


/*
Solution 1
TRUNCATE(SUM()) / WHERE clause
*/
SELECT
    TRUNCATE(SUM(lat_n), 4)
FROM
    station
WHERE
    -- BETWEEN conditional is inclusive
    lat_n BETWEEN 38.7881 AND 137.2344
;


/*
Solution 2
TRUNCATE(SUM()) / CASE statement
*/
SELECT
    TRUNCATE(SUM(CASE WHEN lat_n > 38.7880 AND
                        lat_n < 137.2345
                        THEN lat_n
                        ELSE 0 END), 4)
        AS all_lat_n
FROM
    station
;


/*
Solution 3
TRUNCATE(SUM()) / SQ: WHERE clause
*/
SELECT
    TRUNCATE(SUM(lat_n), 4)
FROM
    (SELECT
        lat_n
    FROM
        station
    WHERE
        lat_n > 38.7880 AND
        lat_n < 137.2345)
        AS all_lat_n
;