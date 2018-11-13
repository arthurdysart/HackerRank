/*
HackerRank SQL: Type of Triangle
https://www.hackerrank.com/challenges/what-type-of-triangle
Difficulty: easy

Created on Sun Oct 28 17:42:12 2018
@author: Arthur Dysart
*/


/*
Solution 1
CASE statements, cascading
*/
SELECT 
    -- Checks the triangle inequality theorem
    CASE
        WHEN (A+B)<=C THEN 'Not A Triangle'
        WHEN (A+C)<=B THEN 'Not A Triangle'
        WHEN (C+B)<=A THEN 'Not A Triangle'
        -- Checks if equilateral triangle
        WHEN (A=B AND A=C) THEN 'Equilateral'
        -- Checks if scalene triangle
        WHEN (A!=B AND A!=C AND B!=C) THEN 'Scalene'
        -- Checks if isosceles triangle
        WHEN (A=B AND A!=C) THEN 'Isosceles'
        WHEN (A=C AND A!=B) THEN 'Isosceles'
        WHEN (C=B AND A!=C) THEN 'Isosceles'
        ELSE 'Not A Triangle'
    END
FROM TRIANGLES;


/*
Solution 2
COALESCE / CASE statements, cascading
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