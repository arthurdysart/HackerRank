/*
HackerRank SQL: Type of Triangle
https://www.hackerrank.com/challenges/what-type-of-triangle
Difficulty: easy

Created on Sun Oct 28 17:42:12 2018
@author: Arthur Dysart
*/

-- Evaluates sequentially until non-null result
SELECT COALESCE(
    -- Checks the triangle inequality theorem
    CASE WHEN (A+B)<=C THEN 'Not A Triangle' ELSE NULL END,
    CASE WHEN (A+C)<=B THEN 'Not A Triangle' ELSE NULL END,
    CASE WHEN (C+B)<=A THEN 'Not A Triangle' ELSE NULL END,
    -- Checks if equilateral triangle
    CASE WHEN (A=B AND A=C) THEN 'Equilateral' ELSE NULL END,
    -- Checks if scalene triangle
    CASE WHEN (A!=B AND A!=C AND B!=C) THEN 'Scalene' ELSE NULL END,
    -- Checks if isosceles triangle
    CASE WHEN (A=B AND A!=C) THEN 'Isosceles' ELSE NULL END,
    CASE WHEN (A=C AND A!=B) THEN 'Isosceles' ELSE NULL END,
    CASE WHEN (C=B AND A!=C) THEN 'Isosceles' ELSE NULL END,
    -- Returns non-triangle result
    CASE WHEN True THEN 'Not A Triangle' END)
FROM TRIANGLES;