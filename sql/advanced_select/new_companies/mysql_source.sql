/*
HackerRank SQL: New Companies
https://www.hackerrank.com/challenges/the-company
Difficulty: medium

Created on Fri Dec  7 23:13:14 2018
@author: Arthur Dysart
*/

/*
Solution 1
LEFT JOIN, COUNT(DISTINCT), GROUP BY, ORDER BY
*/

SELECT
    c.company_code,
    c.founder,
    COUNT(DISTINCT lm.lead_manager_code)
        AS number_lead_managers,
    COUNT(DISTINCT sm.senior_manager_code)
        AS number_senior_managers,
    COUNT(DISTINCT m.manager_code)
        AS number_managers,
    COUNT(DISTINCT e.employee_code)
        AS number_employees
FROM
    company
        AS c
LEFT JOIN
    lead_manager
        AS lm
    ON c.company_code = lm.company_code
LEFT JOIN
    senior_manager
        AS sm
    ON c.company_code = sm.company_code
LEFT JOIN
    manager
        AS m
    ON c.company_code = m.company_code
LEFT JOIN
    employee
        AS e
    ON c.company_code = e.company_code
GROUP BY
    c.company_code,
    c.founder
ORDER BY
    c.company_code
        ASC
;