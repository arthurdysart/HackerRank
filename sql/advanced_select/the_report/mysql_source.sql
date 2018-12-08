/*
HackerRank SQL: The Report
https://www.hackerrank.com/challenges/the-report
Difficulty: medium

Created on Fri Dec  7 23:34:01 2018
@author: Arthur Dysart
*/

/*
Solution 1
CASE STATEMENT, LEFT JOIN, BETWEEN, ORDER BY
*/

SELECT
    CASE
        WHEN
            g.grade >= 8
              THEN s.name
        ELSE NULL
    END
        AS name,
    g.grade
        AS grade,
    s.marks
        AS marks    
FROM
    students
        AS s
LEFT JOIN
    grades
        AS g
    ON s.marks
        BETWEEN
          g.min_mark AND g.max_mark
ORDER BY
    g.grade
        DESC,
    s.name
        ASC
;