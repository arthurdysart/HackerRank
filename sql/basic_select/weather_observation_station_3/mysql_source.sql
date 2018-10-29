/*
HackerRank SQL: Weather Observation Station 3
https://www.hackerrank.com/challenges/weather-observation-station-3
Difficulty: easy

Created on Sun Oct 28 16:18:07 2018
@author: Arthur Dysart
*/

-- Selects distinct "CITY" attribute values
SELECT DISTINCT CITY
FROM STATION
-- Selects by "ID" attributes which are even
WHERE MOD(ID,2)=0;