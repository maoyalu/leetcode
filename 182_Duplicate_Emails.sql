/* ********** Attempt 1 - 2019/09/21  ********** */

SELECT Email
FROM Person
GROUP BY Email
HAVING COUNT(*) > 1