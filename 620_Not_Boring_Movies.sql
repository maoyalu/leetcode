/* ********** Attempt 1 - 2019/09/21  ********** */

SELECT id, movie, description, rating
FROM cinema
WHERE id % 2 != 0 AND description != 'boring'
ORDER BY rating DESC