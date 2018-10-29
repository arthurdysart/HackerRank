/*
HackerRank SQL: Binary Tree Nodes
https://www.hackerrank.com/challenges/binary-search-tree-1
Difficulty: medium

Created on Sun Oct 28 19:44:54 2018
@author: Arthur Dysart
*/

-- Evaluates sequentially until non-null result
SELECT COALESCE(
    -- Checks if no parent exists
    CASE WHEN (P IS null) THEN CONCAT(N, ' Root') ELSE NULL END,
    -- Checks if node is not parent of other nodes 
    CASE WHEN N IN (SELECT DISTINCT P FROM BST) THEN CONCAT(N, ' Inner') ELSE NULL END,
    -- Returns node as inner node
    CASE WHEN True THEN CONCAT(N, ' Leaf') END)
FROM BST
ORDER BY N ASC;