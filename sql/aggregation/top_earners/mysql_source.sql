/*
HackerRank SQL: Top Earners
https://www.hackerrank.com/challenges/earnings-of-employees
Difficulty: easy

Created on Mon Nov 12 12:08:54 2018
@author: Arthur Dysart
*/

/*
Solution 1
GROUP BY / ORDER BY / LIMIT
*/
SELECT
    months * salary
        AS total_earnings,
    COUNT(employee_id)
FROM 
    employee
GROUP BY
    total_earnings
ORDER BY
    total_earnings DESC
LIMIT
    1
;


/*
Solution 2
WHERE / Subquery: MAX()
*/
SELECT
    MAX(months * salary)
        AS maximum_total_earnings,
    COUNT(employee_id)
        AS employees_max_earnings
FROM 
    employee
WHERE
    -- Aliases illegal in WHERE clause
    months * salary = (
        -- SQ: Find maximum total earnings
        SELECT
            MAX(months * salary)
        FROM
            employee)
;