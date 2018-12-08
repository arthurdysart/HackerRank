/*
HackerRank SQL: Top Competitors
https://www.hackerrank.com/challenges/full-score
Difficulty: medium

Created on Sat Dec  8 11:42:59 2018
@author: Arthur Dysart
*/

/*
Solution 1
LEFT JOIN, WHERE, GROUP BY, HAVING, ORDER BY
*/
SELECT
    s.hacker_id,
    h.name
FROM
    submissions
        AS s
LEFT JOIN
    hackers
        AS h
    ON s.hacker_id = h.hacker_id
LEFT JOIN
    challenges
        AS c
    ON s.challenge_id = c.challenge_id
LEFT JOIN
    difficulty
        AS d
    ON c.difficulty_level = d.difficulty_level
WHERE
    s.score = d.score
GROUP BY
    s.hacker_id,
    h.name
HAVING
    COUNT(*) > 1
ORDER BY
    COUNT(*)
        DESC,
    hacker_id
        ASC
;